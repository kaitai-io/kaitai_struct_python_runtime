import struct
from _typeshed import Incomplete
from enum import Enum
from io import BytesIO
from mmap import mmap
from typing import Any, Callable, List, Optional, Type, TypeVar, Union
API_VERSION = (0, 11)

KTStruct = TypeVar("KTStruct", bound="KaitaiStruct")
KTStream = TypeVar("KTStream", bound="KaitaiStream")

class KaitaiStruct:
    """
    The KaitaiStruct class represents a Kaitai Struct binary format parser.

    Parameters:
    - stream: A KTStream object representing the input stream from which the binary data will be parsed.

    Methods:
    - __init__(self, stream: KTStream) -> None:
      Initializes a new KaitaiStruct object.

    - __enter__(self) -> KTStruct:
      Context manager method that allows the KaitaiStruct object to be used in a "with" statement.

    - __exit__(self, *args, **kwargs) -> None:
      Context manager method that is called when exiting a "with" statement.

    - close(self) -> None:
      Closes the KaitaiStruct object and releases any resources associated with it.

    - from_file(cls, filename: str) -> KTStruct:
      Creates a new KaitaiStruct object from a file specified by the filename parameter.

    - from_bytes(cls, buf: mmap) -> KTStruct:
      Creates a new KaitaiStruct object from a byte buffer specified by the buf parameter.

    - from_io(cls, io: Union[BytesIO, mmap]) -> KTStruct:
      Creates a new KaitaiStruct object from an input stream specified by the io parameter.
    """

    def __init__(self, stream: KTStream) -> None:
        """
        :param stream: A Kaitai stream object representing the input stream to parse.
        :type stream: KTStream

        Initializes a KaitaiStruct object with the given stream.
        """
        self._io: KTStream = ...

        ...
    def __enter__(self) -> KTStruct:
        """
        Enter the context manager.

        :returns: An instance of KTStruct representing the entered context.
        :rtype: KTStruct
        """
        ...
    def __exit__(self, *args, **kwargs) -> None:
        """
        Context management method that is called when exiting the 'with' statement block.

        :param args: The positional arguments passed to the method.
        :param kwargs: The keyword arguments passed to the method.
        :return: None
        """
        ...
    def close(self) -> None:
        """
        Close the KaitaiStruct instance and release any associated resources.

        :return: None
        """
        ...
    @classmethod
    def from_file(cls, filename: str) -> KTStruct:
        """
        :param filename: The name of the file to read from.
        :return: An instance of KaitaiStruct with a KaiStream object representing the contents of the file.

        This method reads the contents of a file and returns an instance of the KaitaiStruct subclass that represents the data in the file.
        """
        ...
    @classmethod
    def from_bytes(cls, buf: mmap) -> KTStruct:
        """
        Converts a memory-mapped file, represented by `buf`, into an instance of `KTStruct`.

        :param buf: The memory-mapped file to convert.
        :return: An instance of `KTStruct` representing the contents of the memory-mapped file.
        """
        ...
    @classmethod
    def from_io(cls, io: Union[BytesIO, mmap]) -> KTStruct:
        """ """
        ...

class ReadWriteKaitaiStruct(KaitaiStruct):
    """A class to read and write data using the Kaitai Struct format.

    This class extends the base KaitaiStruct class to add functionality for writing data.

    Attributes:
        See the base KaitaiStruct class for the list of inherited attributes.

    Methods:
        write_<datatype>: Write a value of the specified data type to the underlying data stream.
    """

    ...

class KaitaiStream:
    """ """


    def __init__(self, io: mmap) -> None:
        """
        __init__(io: mmap)

        Initialize a new instance of KaitaiStream.

        :param io: A memory-mappable file object to read from. It must be an instance of mmap.
        """
        self._io: mmap = ...
        self.bits: int = ...
        self.bits_left: int = ...

        self.bits_le: bool = ...
        self.bits_write_mode: bool = ...

        self.write_back_handler: Optional[callable] = ...
        self.child_streams: List[KTStream] = ...
        self._size: Optional[int] = ...
        ...
    def __enter__(self) -> KTStream:
        """
        Subclass of BytesIO that implements __enter__ and __exit__ methods for use as a context manager.

        Usage:
        with KaitaiStream(data) as ks:
            # Perform operations on ks

        :return: A KaitaiStream object.
        :rtype: KaitaiStream
        """
        ...
    def __exit__(self, *args, **kwargs) -> None:
        """
        :param args: Tuple of positional arguments passed to the method.
        :param kwargs: Dictionary of keyword arguments passed to the method.
        :return: None

        The __exit__ method is a special method in the `KaitaiStream` class. It is called when exiting a context managed by a `with` statement. This method allows for any necessary cleanup or finalization operations to be performed.

        Usage example:
        ```
        with KaitaiStream() as stream:
            # Code within the context managed by the `with` statement
            # ...

        # After the code block completes or raises an exception,
        # the __exit__ method is automatically called.
        ```
        """
        ...
    def close(self) -> None:
        """
        Close the KaitaiStream object.

        :return: None
        """
        ...
    def is_eof(self) -> bool:
        """
        Check if the stream is at the end of the file.

        Returns:
            True if the stream is at the end of the file, False otherwise.
        """
        ...
    def seek(self, n: int) -> None:
        """
        Seek to a position in the stream.

        Args:
            n: Position to seek to.
        """
        ...
    def pos(self) -> int:
        """
        Get the current position in the stream.

        Returns:
            Current position in the stream.
        """
        ...
    def size(self) -> int:
        """
        Get the size of the stream.

        Returns:
            Size of the stream.
        """
        ...
    packer_s1: struct.Struct
    packer_s2be: struct.Struct
    packer_s4be: struct.Struct
    packer_s8be: struct.Struct
    packer_s2le: struct.Struct
    packer_s4le: struct.Struct
    packer_s8le: struct.Struct
    packer_u1: struct.Struct
    packer_u2be: struct.Struct
    packer_u4be: struct.Struct
    packer_u8be: struct.Struct
    packer_u2le: struct.Struct
    packer_u4le: struct.Struct
    packer_u8le: struct.Struct
    packer_f4be: struct.Struct
    packer_f8be: struct.Struct
    packer_f4le: struct.Struct
    packer_f8le: struct.Struct
    def read_s1(self) -> int:
        """
        Read a signed 1-byte integer from the stream.

        :return: The read value as an integer.
        :rtype: int
        """
        ...
    def read_s2be(self) -> int:
        """
        Read a signed 2-byte big-endian integer from the stream.

        :return: The read value as an integer.
        :rtype: int
        """
        ...
    def read_s4be(self) -> int:
        """
        Read a signed 4-byte big-endian integer from the stream.

        :return: The read value as an integer.
        """
        ...
    def read_s8be(self) -> int:
        """
        Reads a signed 8-bit integer in big-endian format from the stream.

        :return: The signed 8-bit integer value read from the stream.
        :rtype: int
        """
        ...
    def read_s2le(self) -> int:
        """Reads a signed 2-byte little-endian integer from the stream.

        :return: The signed 2-byte little-endian integer read from the stream.
        :rtype: int
        """
        ...
    def read_s4le(self) -> int:
        """Read a 4-byte signed integer in little-endian format.

        :return: The 4-byte signed integer read from the stream.
        :rtype: int
        """
        ...
    def read_s8le(self) -> int:
        """
        Read a signed 8-bit integer in little-endian format from the stream.

        :return: The signed 8-bit integer read from the stream as an integer value.
        """
        ...
    def read_u1(self) -> int:
        """
        Reads and returns an unsigned 1-byte integer from the stream.

        :return: The read unsigned 1-byte integer.
        """
        ...
    def read_u2be(self) -> int:
        """
        Reads and interprets a 2-byte unsigned big-endian integer from the stream.

        :return: The 2-byte unsigned big-endian integer read from the stream.
        """
        ...
    def read_u4be(self) -> int:
        """
        Reads a 4-byte big-endian unsigned integer from the stream.

        :return: The value of the 4-byte big-endian unsigned integer read from the stream.
        :rtype: int
        """
        ...
    def read_u8be(self) -> int:
        """
        Reads an unsigned 8-bit integer (big endian) from the underlying stream.

        :return: The value of the unsigned 8-bit integer.
        :rtype: int
        """
        ...
    def read_u2le(self) -> int:
        """
        Reads a 2-byte unsigned integer value in little-endian format from the current position of the stream.

        :return: The 2-byte unsigned integer value read from the stream.
        :rtype: int
        """
        ...
    def read_u4le(self) -> int:
        """
        Reads a 4-byte unsigned integer in little-endian format from the stream.

        :return: The 4-byte unsigned integer read from the stream.
        :rtype: int
        """
        ...
    def read_u8le(self) -> int:
        """
        Reads an unsigned 8-bit integer from the stream in little-endian byte order.

        :return: The unsigned 8-bit integer.
        """
        ...
    def read_f4be(self) -> float:
        """
        Reads and returns a 4-byte big-endian floating point number from the current position in the KaitaiStream.

        :return: A 4-byte big-endian floating point number read from the stream.
        :rtype: float
        """
        ...
    def read_f8be(self) -> float:
        """
        Reads an 8-byte floating point number in big-endian format from the KaitaiStream.

        :return: The 8-byte floating point number read from the KaitaiStream.
        :rtype: float
        """
        ...
    def read_f4le(self) -> float:
        """
        Reads a 4-byte floating-point value from the KaitaiStream.

        :return: A floating-point value read from the stream.
        """
        ...
    def read_f8le(self) -> float:
        """
        Reads an 8-byte floating-point value from the stream in little-endian format.

        :return: The read floating-point value.
        :rtype: float
        """
        ...
    def align_to_byte(self) -> None:
        """
        Aligns the current position of the KaitaiStream object to the nearest byte boundary.

        :return: None
        """
        ...
    def read_bits_int_be(self, n: int) -> int:
        """
        Reads and returns an integer value from the stream by reading `n` bits in big-endian format.

        :param n: Number of bits to read
        :return: Integer value read from the stream
        """
        ...
    def read_bits_int(self, n: int) -> int:
        """
        Reads an integer value from the stream as a specified number of bits.

        :param n: The number of bits to read.
        :return: The integer value read from the stream.
        """
        ...
    def read_bits_int_le(self, n: int) -> int:
        """
        Reads an unsigned integer of length `n` bits from the stream in little-endian format.

        :param n: The number of bits to read.
        :return: The unsigned integer value.

        """
        ...
    def read_bytes(self, n: int) -> bytes:
        """
        :param n: The number of bytes to read from the stream.
        :return: The bytes read from the stream.

        """
        ...

    def _read_bytes_not_aligned(self, n: int) -> bytes:
        """
        Reads a specified number of bytes from the stream.

        :param n: The number of bytes to read.
        :return: The bytes read from the stream.
        """
        ...
    def read_bytes_full(self):
        """
        Reads and returns all available bytes in the stream.

        :return: All available bytes in the stream.
        :rtype: bytes
        """
        ...
    def read_bytes_term(
        self, term: int, include_term: bool, consume_term: bool, eos_error: bool
    ) -> bytes:
        """
        Reads bytes from the stream until a specific termination condition is met.

        :param term: The termination condition (byte value or ordinal).
        :param include_term: If True, includes the termination byte in the returned bytes. Otherwise, excludes it.
        :param consume_term: If True, consumes the termination byte from the stream. Otherwise, keeps it in the stream.
        :param eos_error: If True and end of stream is encountered before the termination condition, raises an error. Otherwise, returns the bytes read until that point.
        :return: The bytes read from the stream.

        :rtype: bytes
        """
        ...
    def ensure_fixed_contents(self, expected: bytes) -> bytes:
        """
        Ensures that the given `expected` bytes are present in the stream.

        :param expected: The bytes to be checked in the stream.
        :type expected: bytes
        :return: The bytes if found in the stream.
        :rtype: bytes
        """
        ...
    @staticmethod
    def bytes_strip_right(data: bytes, pad_byte: int) -> bytes:
        """
        Strip trailing padding bytes from the given data.

        :param data: The input bytes to be stripped.
        :param pad_byte: The byte value used for padding.
        :return: The data with trailing padding bytes stripped.
        """
        ...
    @staticmethod
    def bytes_terminate(data: bytes, term: int, include_term: bool) -> bytes:
        """
        :param data: The input bytes data that needs to be terminated.
        :param term: The termination character or byte value.
        :param include_term: A boolean flag indicating whether to include the termination character in the result.
        :return: The terminated bytes data.

        This method `bytes_terminate` takes in a `data` parameter which is a bytes object representing the input data that needs to be terminated. The `term` parameter defines the termination character or byte value. The `include_term` parameter is a boolean flag indicating whether the termination character should be included in the result or not.

        The return value of this method is a bytes object that represents the terminated data. If `include_term` is `True`, the termination character will be included in the result; otherwise, it will be excluded.

        Example usage:

        ```python
        data = b'Hello, world!'
        term = 0x00
        include_term = True
        result = KaitaiStream.bytes_terminate(data, term, include_term)
        print(result)  # Output: b'Hello, world!\x00'
        ```
        """
        ...
    def write_s1(self, v: int) -> None:
        """
        Write a single signed 1-byte integer value to the output stream.

        :param v: The value to be written.
        :return: None

        """
        ...
    def write_s2be(self, v: int) -> None:
        """
        Write the given 16-bit signed integer in big-endian byte order to the
        output stream.

        :param v: The 16-bit signed integer to write.
        :type v: int
        :return: None
        """
        ...
    def write_s4be(self, v: int) -> None:
        """
        Write an int value in signed 4-byte big-endian encoding to the output stream.

        :param v: The int value to be written.
        :return: None
        """
        ...
    def write_s8be(self, v: int) -> None:
        """
        Writes a signed 8-bit integer in big-endian format to the stream.

        :param v: The signed 8-bit integer value to write.
        :type v: int
        :return: None
        """
        ...
    def write_s2le(self, v: int) -> None:
        """
        Writes a signed 2-byte integer value (`v`) to the stream in little-endian format.

        :param v: The value to be written.
        :return: None
        """
        ...
    def write_s4le(self, v: int) -> None:
        """
        Writes a 32-bit signed integer in little-endian byte order to the underlying stream.

        :param v: The value to write.
        :type v: int
        :return: None
        :rtype: None

        """
        ...
    def write_s8le(self, v: int) -> None:
        """
        Writes a signed 8-bit integer in little-endian format to the stream.

        :param v: The signed 8-bit integer value to write.
        :type v: int

        :return: None
        :rtype: None

        """
        ...
    def write_u1(self, v: int) -> None:
        """
        Writes a 1-byte unsigned integer to the KaitaiStream.

        :param v: The value to be written as a 1-byte unsigned integer.
        :return: None
        """
        ...
    def write_u2be(self, v: int) -> None:
        """
        Write a 2-byte unsigned integer in big-endian byte order to the stream.

        :param v: The value to write.
        :return: None

        """
        ...
    def write_u4be(self, v: int) -> None:
        """
        Write a 4-byte unsigned integer in big-endian byte order to the underlying stream.

        :param v: The value to be written.
        :return: None
        """
        ...
    def write_u8be(self, v: int) -> None:
        """
        Writes an unsigned 8-bit integer (big endian) to the underlying stream.

        :param v: The value to be written.
        :type v: int
        :return: None
        """
        ...
    def write_u2le(self, v: int) -> None:
        """

        .. method:: KaitaiStream.write_u2le(v: int) -> None

            This method writes an unsigned 2-byte integer in little-endian format to the stream.

            :param v: The value to be written.
            :type v: int
            :return: None

        """
        ...
    def write_u4le(self, v: int) -> None:
        """
        Write a 4-byte unsigned integer (little-endian) to the output stream.

        :param v: The value to write.
        :return: None

        """
        ...
    def write_u8le(self, v: int) -> None:
        """
        Write an unsigned 8-bit integer in little-endian byte order to the underlying stream.

        :param v: The value to write, must be within the range [0, 255].
        :return: None
        """
        ...
    def write_f4be(self, v: float) -> None:
        """
        Writes a 4-byte floating point value in big endian format to the output stream.

        :param v: The 4-byte floating point value to write.
        :type v: float
        :return: None
        """
        ...
    def write_f8be(self, v: float) -> None:
        """
        Write a float value in 8-byte big-endian format to the current position in the output stream.

        :param v: The float value to write
        :return: None

        """
        ...
    def write_f4le(self, v: float) -> None:
        """
        Writes a 4-byte little-endian (f4le) floating-point value to the output stream.

        :param v: The floating-point value to be written to the stream.
        :type v: float
        :return: None
        """
        ...
    def write_f8le(self, v: float) -> None:
        """
        Writes a 8-byte floating-point value in little-endian format to the output stream.

        :param v: The float value to write.
        :type v: float
        :return: None
        :rtype: None
        """
        ...
    def write_align_to_byte(self) -> None:
        """
        Write a zero byte padding to the current position in the output stream, if necessary,
        in order to align the position to the next byte boundary.

        :return: None
        """
        ...

    def _write_bytes_not_aligned(self, buf: Union[bytes, bytearray]) -> None:
        """
        Writes the given bytes to the stream.

        :param buf: The bytes to write.
        :return: None
        """
        ...

    def _write_bits_int(self, n: int, val: int) -> None:
        """
        Writes an integer value to the stream as a specified number of bits.

        :param n: The number of bits to write.
        :param val: The integer value to write.
        :return: None
        """
        ...

    def _ensure_bytes_left_to_write(self, n: int, pos: int) -> None:
        """
        Ensures that the specified number of bytes are available to write to the stream.

        :param n: The number of bytes to write.
        :param pos: The current position in the stream.
        :return: None
        """
        ...
    def write_bits_int_be(self, n: int, val: int) -> None:
        """
        Write bits of an integer value in big-endian order to the output stream.

        :param n: Number of bits to write.
        :param val: Integer value to write.
        :return: None

        Example Usage:
        stream = KaitaiStream()
        stream.write_bits_int_be(8, 255)
        """
        ...
    def write_bits_int_le(self, n: int, val: int) -> None:
        """
        Writes an `n`-bit integer value in little-endian format to the stream.

        :param n: The number of bits to write.
        :type n: int
        :param val: The integer value to write.
        :type val: int
        :return: None
        :rtype: None
        """
        ...
    def write_bytes(self, buf: Union[bytes, bytearray]) -> None:
        """
        Write bytes to the underlying binary stream.

        :param buf: The bytes to be written.
        :type buf: Union[bytes, bytearray]
        :return: None
        :rtype: None
        """
        ...
    def write_bytes_limit(
        self, buf: Union[bytes, bytearray], size: int, term: int, pad_byte: int
    ) -> None:
        """
        Writes a limited number of bytes from the given buffer to the stream.

        :param buf: The buffer containing the bytes to write.
        :type buf: Union[bytes, bytearray]
        :param size: The maximum number of bytes to write from the buffer.
        :type size: int
        :param term: The termination marker indicating the end of the data in the buffer.
        :type term: int
        :param pad_byte: The byte value used for padding if the size limit is not reached.
        :type pad_byte: int
        :return: None
        """
        ...
    @staticmethod
    def process_xor_one(data: Union[bytes, bytearray], key: int) -> bytes:
        """
        :param data: The input data to be XORed.
        :param key: The key used for XOR operation.
        :return: The XORed bytes.

        This method takes in a sequence of bytes represented by either a bytes or bytearray object,
        and performs a XOR operation on each byte of the input data using the provided key. The key
        should be an integer value.

        The method returns the result of the XOR operation as a bytes object.


        """
        ...
    @staticmethod
    def process_xor_many(
        data: Union[bytes, bytearray], key: Union[bytes, bytearray]
    ) -> bytes:
        """
        :param data: The input data to be processed.
        :param key: The XOR key used for encryption.
        :return: The processed data after XOR encryption.

        This method takes an input data and performs XOR encryption using the specified key. It returns the processed data as the result of the XOR operation.
        """
        ...
    @staticmethod
    def process_rotate_left(
        data: Union[bytes, bytearray], amount: int, group_size: int
    ) -> bytes:
        """
        :method process_rotate_left:
        :param data: The input data to rotate left.
        :param amount: The number of positions to rotate the data left.
        :param group_size: The size of each rotating group.
        :return: The rotated data.

        This method takes in input data and rotates it left by the specified number of positions. The rotation is done in groups of the specified size.
        The method returns the rotated data.

        :type data: Union[bytes, bytearray]
        :type amount: int
        :type group_size: int
        :return: bytes
        """
        ...
    @staticmethod
    def int_from_byte(v: Union[bytes, bytearray]) -> int:
        """
        Converts a byte or bytearray value to an integer.

        :param v: The byte or bytearray value to convert.
        :return: The converted integer value.

        """
        ...
    @staticmethod
    def byte_from_int(i: int) -> bytes:
        """
        :param i: an integer value representing a byte
        :return: a bytes object representing the input integer value as a single byte
        """
        ...
    @staticmethod
    def byte_array_index(data: Union[bytes, bytearray], i: int) -> int:
        """
        :param data: The byte array or byte string to search in.
        :param i: The index to search for in the byte array.
        :return: The index of the first occurrence of `i` in `data`. If `i` is not found, returns -1.
        """
        ...
    @staticmethod
    def byte_array_min(b: Union[bytes, bytearray]) -> int:
        """
        :param b: The byte array to find the minimum value in.
        :type b: Union[bytes, bytearray]
        :return: The minimum value in the byte array.
        :rtype: int
        """
        ...
    @staticmethod
    def byte_array_max(b: Union[bytes, bytearray]) -> int:
        """
        :param b: A byte array.
        :return: The maximum value of the byte array.
        """
        ...
    @staticmethod
    def byte_array_index_of(data: Union[bytes, bytearray], b: int) -> int:
        """
        :param data: The byte array in which to search for the specified byte.
        :type data: Union[bytes, bytearray]
        :param b: The byte to search for in the byte array.
        :type b: int
        :return: The index of the first occurrence of the specified byte in the byte array, or -1 if the byte is not found.
        :rtype: int
        """
        ...
    @staticmethod
    def resolve_enum(enum_obj: Type[Enum], value: int) -> Any:
        """
        Resolves an enum value based on its integer value.

        :param enum_obj: The enum class.
        :type enum_obj: Type[Enum]
        :param value: The integer value of the enum.
        :type value: int
        :return: The enum value corresponding to the provided integer value.
        :rtype: Any
        """
        ...
    def to_byte_array(self) -> bytes:
        """
        Convert the KaitaiStream object to a byte array.

        :return: A byte array representation of the KaitaiStream object.
        :rtype: bytes
        """
        ...

    class WriteBackHandler:
        """ """

        pos: Incomplete
        handler: Incomplete
        def __init__(self, pos: int, handler: Callable[[KTStream], None]) -> None: ...
        def write_back(self, parent: KTStream) -> None: ...

    def add_child_stream(self, child: WriteBackHandler) -> None:
        """
        :param child: A child stream to be added to the current stream.
        :return: None
        """
        ...
    def write_back_child_streams(self, parent: Union[KTStream, None] = ...) -> None:
        """
        Write back child streams.

        :param parent: The parent stream object to write back to.
        :return: None
        """
        ...

    def _write_back(self, parent: KTStream) -> None:
        """
        Write back the current stream to the parent stream.

        :param parent: The parent stream object to write back to.
        :return: None
        """
        ...

class KaitaiStructError(Exception): ...

class UndecidedEndiannessError(KaitaiStructError): ...

class ValidationFailedError(KaitaiStructError): ...

class ValidationNotEqualError(ValidationFailedError): ...

class ValidationLessThanError(ValidationFailedError): ...

class ValidationGreaterThanError(ValidationFailedError): ...

class ValidationNotAnyOfError(ValidationFailedError):
        ...

class ValidationExprError(ValidationFailedError): ...

class ConsistencyError(Exception): ...
