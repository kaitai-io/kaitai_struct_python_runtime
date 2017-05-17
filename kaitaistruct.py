import itertools
import sys
from struct import unpack

try:
    import cStringIO
    BytesIO = cStringIO.StringIO
except ImportError:
    from io import BytesIO  # noqa

PY2 = sys.version_info[0] == 2

# Kaitai Struct runtime streaming API version, defined as per PEP-0396
# standard. Used for two purposes:
#
# * .py files generated by ksc from .ksy check that they import proper
#   KS runtime library by this version number;
# * distribution utils (setup.py) use this when packaging for PyPI
#
__version__ = '0.7'


class KaitaiStruct(object):
    def __init__(self, stream):
        self._io = stream

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    @classmethod
    def from_file(cls, filename):
        f = open(filename, 'rb')
        try:
            return cls(KaitaiStream(f))
        except Exception:
            # close file descriptor, then reraise the exception
            f.close()
            raise

    def close(self):
        self._io.close()

class Endianness:
    """Just stores the description of endianness"""
    def __init__(self, name, char):
       self.name=name
       self.char=char

class KaitaiType:
    """Represents a type, which can take a finite set of fixed lengths and available to 'struct' module. This class is used to store the info to generate them automatically."""
    endianessesTable=[
        Endianness("le", "<"),
        Endianness("be", ">")
    ]

    def readFuncFac(fStr, size):
        def read(self):
            return unpack(fStr, self.read_bytes(size))[0]
        return read

    funcFactories=(readFuncFac)

    def __init__(self, typeName:str=None, sizesTable:dict=None):
        self.typeName=typeName # the first letter must identify the type for KS
        if sizesTable:
            self.sizesTable=sizesTable
        else:
            self.sizesTable={}
    
    def makeAccessorFunc(self, size, endianess, factory):
        fStr="".join((endianess.char, self.sizesTable[size]))
        func=factory(fStr, size)
        func.__doc__="".join((
            func.__name__, "s ",
            str(size), "-byte ",
            endianess.name, " ", self.typeName, "s"
        ))
        func.__name__="".join((func.__name__,"_", self.typeName[0], str(size), endianess.name))
        return func
    
    def generateAccessorFunctions(self):
        for endianness in self.endianTable:
            for size in self.sizesTable.keys():
                for fac in self.funcFactories:
                    yield self.makeAccessorFunc(size, endianness, fac)
    
default_types_table={
    KaitaiType(
        "unsigned int",
        {
            1: "B",
            2: "H",
            4: "I",
            8: "Q",
        }
    ),
    KaitaiType(
        "signed int",
        {
            1: "b",
            2: "h",
            4: "i",
            8: "q",
        }
    ),
    KaitaiType(
        "float",
        {
            4: "f",
            8: "d",
        }
    )
}

def _kaitai_stream(name, parents, attrs):
    """A metaclass to generate properties for KaitaiStream classes"""
    if "types_table" not in attrs:
        attrs["types_table"]=default_types_table
    for t in attrs["types_table"]:
        for func in t.generateAccessorFunctions():
            attrs[func.__name__]=func
    return type(name, parents, attrs)

class KaitaiStream(metaclass=_kaitai_stream):
    def __init__(self, io):
        self._io = io
        self.align_to_byte()

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def close(self):
        self._io.close()

    # ========================================================================
    # Stream positioning
    # ========================================================================

    def is_eof(self):
        io = self._io
        t = io.read(1)
        if t == b'':
            return True
        else:
            io.seek(io.tell() - 1)
            return False

    def seek(self, n):
        self._io.seek(n)

    def pos(self):
        return self._io.tell()

    def size(self):
        # Python has no internal File object API function to get
        # current file / StringIO size, thus we use the following
        # trick.
        io = self._io

        # Remember our current position
        cur_pos = io.tell()

        # Seek to the end of the File object
        io.seek(0, 2)

        # Remember position, which is equal to the full length
        full_size = io.tell()

        # Seek back to the current position
        io.seek(cur_pos)

        return full_size
    
    # ========================================================================
    # Unaligned bit values
    # ========================================================================

    def align_to_byte(self):
        self.bits = 0
        self.bits_left = 0

    def read_bits_int(self, n):
        bits_needed = n - self.bits_left
        if bits_needed > 0:
            # 1 bit  => 1 byte
            # 8 bits => 1 byte
            # 9 bits => 2 bytes
            bytes_needed = ((bits_needed - 1) // 8) + 1
            buf = self.read_bytes(bytes_needed)
            for byte in buf:
                # Python 2 will get "byte" as one-character str, thus
                # we need to convert it to integer manually; Python 3
                # is fine as is.
                if isinstance(byte, str):
                    byte = ord(byte)
                self.bits <<= 8
                self.bits |= byte
                self.bits_left += 8

        # raw mask with required number of 1s, starting from lowest bit
        mask = (1 << n) - 1
        # shift mask to align with highest bits available in self.bits
        shift_bits = self.bits_left - n
        mask <<= shift_bits
        # derive reading result
        res = (self.bits & mask) >> shift_bits
        # clear top bits that we've just read => AND with 1s
        self.bits_left -= n
        mask = (1 << self.bits_left) - 1
        self.bits &= mask

        return res

    # ========================================================================
    # Byte arrays
    # ========================================================================

    def read_bytes(self, n):
        r = self._io.read(n)
        if len(r) < n:
            raise EOFError(
                "requested %d bytes, but got only %d bytes" % (n, len(r))
            )
        return r

    def read_bytes_full(self):
        return self._io.read()

    def read_bytes_term(self, term, include_term, consume_term, eos_error):
        r = b''
        while True:
            c = self._io.read(1)
            if c == b'':
                if eos_error:
                    raise Exception(
                        "End of stream reached, but no terminator %d found" %
                        (term,)
                    )
                else:
                    return r
            elif ord(c) == term:
                if include_term:
                    r += c
                if not consume_term:
                    self._io.seek(self._io.tell() - 1)
                return r
            else:
                r += c

    def ensure_fixed_contents(self, expected):
        actual = self._io.read(len(expected))
        if actual != expected:
            raise Exception(
                "Unexpected fixed contents: got %s, was waiting for %s" %
                (str(actual), str(expected))
            )
        return actual

    @staticmethod
    def bytes_strip_right(src, pad_byte):
        new_len = len(src)
        if PY2:
            data = bytearray(src)
        else:
            data = src

        while data[new_len - 1] == pad_byte:
            new_len -= 1

        return data[:new_len]

    @staticmethod
    def bytes_terminate(src, term, include_term):
        new_len = 0
        max_len = len(src)
        if PY2:
            data = bytearray(src)
        else:
            data = src

        while new_len < max_len and data[new_len] != term:
            new_len += 1

        if include_term and new_len < max_len:
            new_len += 1

        return data[:new_len]

    # ========================================================================
    # Byte array processing
    # ========================================================================

    @staticmethod
    def process_xor_one(data, key):
        if PY2:
            r = bytearray(data)
            for i in range(len(r)):
                r[i] ^= key
            return bytes(r)
        else:
            return bytes(v ^ key for v in data)

    @staticmethod
    def process_xor_many(data, key):
        if PY2:
            r = bytearray(data)
            k = bytearray(key)
            ki = 0
            kl = len(k)
            for i in range(len(r)):
                r[i] ^= k[ki]
                ki += 1
                if ki >= kl:
                    ki = 0
            return bytes(r)
        else:
            return bytes(a ^ b for a, b in zip(data, itertools.cycle(key)))

    @staticmethod
    def process_rotate_left(data, amount, group_size):
        if group_size != 1:
            raise Exception(
                "unable to rotate group of %d bytes yet" %
                (group_size,)
            )

        mask = group_size * 8 - 1
        anti_amount = -amount & mask

        r = bytearray(data)
        for i in range(len(r)):
            r[i] = (r[i] << amount) & 0xff | (r[i] >> anti_amount)
        return bytes(r)
