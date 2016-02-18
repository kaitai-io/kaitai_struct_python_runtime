from struct import unpack

class KaitaiStruct:
    def close(self):
        self._io.close()

    def read_u1(self):
        return unpack('B', self._io.read(1))[0]
