from struct import unpack
import array

class KaitaiStruct:
    def close(self):
        self._io.close()

    def ensure_fixed_contents(self, size, expected):
        buf = self._io.read(size)
        actual = array.array('B', buf)
        if actual != expected:
            raise Exception("Unexpected fixed contents: got %s, was waiting for %s" % (str(actual), str(expected)))
        return buf

    def read_u1(self):
        return unpack('B', self._io.read(1))[0]

    def read_s1(self):
        return unpack('b', self._io.read(1))[0]

    def read_u2le(self):
        return unpack('<H', self._io.read(2))[0]

    def read_s2le(self):
        return unpack('<h', self._io.read(2))[0]

    def read_u4le(self):
        return unpack('<I', self._io.read(4))[0]

    def read_s4le(self):
        return unpack('<i', self._io.read(4))[0]

    def read_u8le(self):
        return unpack('<Q', self._io.read(8))[0]

    def read_s8le(self):
        return unpack('<q', self._io.read(8))[0]

    def read_u2be(self):
        return unpack('>H', self._io.read(2))[0]

    def read_s2be(self):
        return unpack('>h', self._io.read(2))[0]

    def read_u4be(self):
        return unpack('>I', self._io.read(4))[0]

    def read_s4be(self):
        return unpack('>i', self._io.read(4))[0]

    def read_u8be(self):
        return unpack('>Q', self._io.read(8))[0]

    def read_s8be(self):
        return unpack('>q', self._io.read(8))[0]

    def read_str_eos(self, encoding):
        return self._io.read().decode(encoding)

    def read_str_byte_limit(self, size, encoding):
        return self._io.read(size).decode(encoding)

    def read_strz(self, encoding, term, include_term, consume_term, eos_error):
        r = ''
        while True:
            c = self._io.read(1)
            if c == '':
                if eos_error:
                    raise Exception("End of stream reached, but no terminator %d found" % (term))
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

    def is_io_eof(self, io):
        t = io.read(1)
        if t == '':
            return True
        else:
            io.seek(io.tell() - 1)
            return False

    @staticmethod
    def process_rotate_left(data, amount, group_size):
        if group_size != 1:
            raise Exception("unable to rotate group of %d bytes yet" % (group_size))

        mask = group_size * 8 - 1
        anti_amount = -amount & mask

        r = array.array('B', data)
        for i in xrange(len(r)):
            r[i] = (r[i] << amount) & 0xff | (r[i] >> anti_amount)
        return r.tostring()
