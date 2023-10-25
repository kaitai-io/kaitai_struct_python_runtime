"""
This test is a proof of concept of a lazy parsing. It has the same benefit as the original one, but it is much faster.
I've added the test file to the repository, so you can run it yourself.
"""

from kaitaistruct import KaitaiStruct
import cProfile
import tracemalloc


class AnftOrig(KaitaiStruct):
    def __init__(self, _io, _parent = None, _root = None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic_bytes = self._io.read_bytes(4)
        self.unknown1 = self._io.read_u1()
        self.num_records = self._io.read_u4le()
        self.records = []
        for i in range(self.num_records):
            self.records.append(Anft.Records(self._io, self, self._root))

        self.footer = self._io.read_bytes(4)

    class Records(KaitaiStruct):
        def __init__(self, _io, _parent = None, _root = None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.first = self._io.read_u8be()
            self.second = self._io.read_u8be()


def old():
    tracemalloc.start()
    cProfile.run("AnftOrig.from_file('test.anft')", sort = "cumtime")
    cur, peak = tracemalloc.get_traced_memory()
    print(f"cur: {cur / 1024 / 1024} MB, peak: {peak / 1024 / 1024} MB")
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)


class Anft(KaitaiStruct):
    def __init__(self, _io, _parent = None, _root = None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self

    @property
    def magic_bytes(self):
        if hasattr(self, "_m_magic_bytes"):
            return self._m_magic_bytes

        self._m_magic_bytes = self._io.read_bytes(4).decode("UTF-8")
        return self._m_magic_bytes

    @property
    def unknown1(self):
        if hasattr(self, "_m_unknown1"):
            return self._m_unknown1

        self._m_unknown1 = self._io.read_u1()
        return self._m_unknown1

    @property
    def num_records(self):
        if hasattr(self, "_m_num_records"):
            return self._m_num_records

        self._m_num_records = self._io.read_u4le()
        return self._m_num_records

    @property
    def records(self):
        if hasattr(self, "_m_records"):
            return self._m_records

        self._m_records = []
        for i in range(self.num_records):
            self._m_records.append(self._root.Records(self._io, self, self._root))

        return self._m_records

    class Records(KaitaiStruct):
        def __init__(self, _io, _parent = None, _root = None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self

        @property
        def first(self):
            if hasattr(self, "_m_first"):
                return self._m_first

            self._m_first = self._io.read_u8be()
            return self._m_first

        @property
        def second(self):
            if hasattr(self, "_m_second"):
                return self._m_second

            self._m_second = self._io.read_u8be()
            return self._m_second


def experimental():
    tracemalloc.start()
    cProfile.run("Anft.from_file('test.anft')", sort = "cumtime")
    cur, peak = tracemalloc.get_traced_memory()
    print(f"cur: {cur / 1024 / 1024} MB, peak: {peak / 1024 / 1024} MB")
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)


# noinspection PyStatementEffect
def experimental2():
    tracemalloc.start()
    cProfile.run("Anft.from_file('test.anft')", sort = "cumtime")
    a = Anft.from_file('test.anft')
    print(a.magic_bytes)
    print(a.unknown1)
    print(a.num_records)
    for i in a.records:
        i.first  # no print to not spam the console
        i.second  # no print to not spam the console

    cur, peak = tracemalloc.get_traced_memory()
    print(f"cur: {cur / 1024 / 1024} MB, peak: {peak / 1024 / 1024} MB")
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)


if __name__ == '__main__':
    """
    The following test is a lazy parsing. It has the same benefit as the original one, but it is much faster.
    It also caches the results of the parsing, so it is even faster on the second run.
    """
    experimental()
    # cur: 1.0425701141357422 MB, peak: 1.0906896591186523 MB

    #          15 function calls in 0.000 seconds
    #
    #    Ordered by: cumulative time
    #
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
    #         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    #         1    0.000    0.000    0.000    0.000 kaitaistruct.py:43(from_file)
    #         1    0.000    0.000    0.000    0.000 {built-in method io.open}
    #         1    0.000    0.000    0.000    0.000 kaitaistruct.py:73(__init__)
    #         1    0.000    0.000    0.000    0.000 contextlib.py:347(__exit__)
    #         1    0.000    0.000    0.000    0.000 kaitaistruct.py:143(size)
    #         1    0.000    0.000    0.000    0.000 {method 'close' of '_io.BufferedReader' objects}
    #         1    0.000    0.000    0.000    0.000 {method 'size' of 'mmap.mmap' objects}
    #         1    0.000    0.000    0.000    0.000 exp_class.py:49(__init__)
    #         1    0.000    0.000    0.000    0.000 {method 'fileno' of '_io.BufferedReader' objects}
    #         1    0.000    0.000    0.000    0.000 contextlib.py:343(__init__)
    #         1    0.000    0.000    0.000    0.000 kaitaistruct.py:272(align_to_byte)
    #         1    0.000    0.000    0.000    0.000 contextlib.py:345(__enter__)
    #         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    #
    #
    # [ Top 10 ]
    # <frozen importlib._bootstrap_external>:729: size=682 KiB, count=5624, average=124 B
    # C:\Python311\Lib\collections\__init__.py:503: size=17.1 KiB, count=90, average=195 B
    # C:\Python311\Lib\opcode.py:36: size=10026 B, count=148, average=68 B
    # C:\Python311\Lib\dataclasses.py:433: size=8524 B, count=100, average=85 B
    # C:\Python311\Lib\ast.py:636: size=7936 B, count=9, average=882 B
    # <frozen importlib._bootstrap>:241: size=7597 B, count=76, average=100 B
    # C:\Python311\Lib\dis.py:49: size=6512 B, count=1, average=6512 B
    # <frozen abc>:106: size=6358 B, count=20, average=318 B
    # C:\Python311\Lib\ast.py:683: size=5462 B, count=10, average=546 B
    # C:\Python311\Lib\collections\__init__.py:436: size=5169 B, count=58, average=89 B
    print("----------------------------------------")
    """
    Next is the comparison of the original with the experimental version.
    """
    # cur: 3.9979352951049805 MB, peak: 4.018841743469238 MB
    old()
    #         57414 function calls in 0.039 seconds
    #
    #    Ordered by: cumulative time
    #
    #    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #         1    0.000    0.000    0.039    0.039 {built-in method builtins.exec}
    #         1    0.000    0.000    0.039    0.039 <string>:1(<module>)
    #         1    0.000    0.000    0.039    0.039 kaitaistruct.py:43(from_file)
    #         1    0.000    0.000    0.039    0.039 exp_class.py:9(__init__)
    #         1    0.034    0.034    0.039    0.039 exp_class.py:15(_read)
    #     28689    0.003    0.000    0.003    0.000 exp_class.py:90(__init__)
    #     28689    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
    #         1    0.000    0.000    0.000    0.000 {built-in method io.open}
    #         4    0.000    0.000    0.000    0.000 kaitaistruct.py:332(read_bytes)
    #         4    0.000    0.000    0.000    0.000 kaitaistruct.py:337(_read_bytes_not_aligned)
    #         1    0.000    0.000    0.000    0.000 contextlib.py:347(__exit__)
    #         1    0.000    0.000    0.000    0.000 kaitaistruct.py:73(__init__)
    #         1    0.000    0.000    0.000    0.000 {method 'close' of '_io.BufferedReader' objects}
    #         4    0.000    0.000    0.000    0.000 {method 'read' of 'mmap.mmap' objects}
    #         1    0.000    0.000    0.000    0.000 kaitaistruct.py:212(read_u1)
    #         1    0.000    0.000    0.000    0.000 kaitaistruct.py:143(size)
    #         1    0.000    0.000    0.000    0.000 kaitaistruct.py:234(read_u4le)
    #         1    0.000    0.000    0.000    0.000 {method 'size' of 'mmap.mmap' objects}
    #         2    0.000    0.000    0.000    0.000 {method 'unpack' of '_struct.Struct' objects}
    #         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    #         4    0.000    0.000    0.000    0.000 {built-in method builtins.len}
    #         1    0.000    0.000    0.000    0.000 contextlib.py:343(__init__)
    #         1    0.000    0.000    0.000    0.000 {method 'fileno' of '_io.BufferedReader' objects}
    #         1    0.000    0.000    0.000    0.000 kaitaistruct.py:272(align_to_byte)
    #         1    0.000    0.000    0.000    0.000 contextlib.py:345(__enter__)
    #
    #
    # [ Top 10 ]
    # D:\Dev\kaitai_struct_python_runtime\experimental\exp_class.py:21: size=2933 KiB, count=57380, average=52 B
    # <frozen importlib._bootstrap_external>:729: size=681 KiB, count=5612, average=124 B
    # C:\Python311\Lib\tracemalloc.py:67: size=46.7 KiB, count=747, average=64 B
    # C:\Python311\Lib\tracemalloc.py:193: size=39.0 KiB, count=832, average=48 B
    # C:\Python311\Lib\collections\__init__.py:503: size=17.1 KiB, count=90, average=195 B
    # C:\Python311\Lib\opcode.py:36: size=10026 B, count=148, average=68 B
    # C:\Python311\Lib\ast.py:636: size=7936 B, count=9, average=882 B
    # <frozen importlib._bootstrap>:241: size=7650 B, count=77, average=99 B
    # C:\Python311\Lib\dataclasses.py:433: size=6820 B, count=69, average=99 B
    # C:\Python311\Lib\dis.py:49: size=6512 B, count=1, average=6512 B

    print("----------------------------------------")
    """
    Bonus
    """
    experimental2()
