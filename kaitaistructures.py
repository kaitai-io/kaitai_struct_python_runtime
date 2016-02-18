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
