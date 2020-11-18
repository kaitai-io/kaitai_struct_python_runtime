# Kaitai Struct: runtime library for Python

[![PyPI](https://img.shields.io/pypi/v/kaitaistruct)](https://pypi.org/project/kaitaistruct/)
![PyPI - Format](https://img.shields.io/pypi/format/kaitaistruct)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/kaitaistruct)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kaitaistruct)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/kaitaistruct)
![PyPI - Downloads](https://img.shields.io/pypi/dd/kaitaistruct)

This library implements Kaitai Struct API for Python.

[Kaitai Struct](http://kaitai.io) is a declarative language used for
describe various binary data structures, laid out in files or in memory:
i.e. binary file formats, network stream packet formats, etc.

It is similar to [Python's Construct 2.9](http://construct.readthedocs.org/)
but it is language-agnostic. The format description is done in YAML-based .ksy
format, which then can be compiled into a wide range of target languages.

Further reading:

* [About Kaitai Struct](http://kaitai.io/)
* [About API implemented in this library](http://doc.kaitai.io/stream_api.html)
* [Python-specific notes](http://doc.kaitai.io/lang_python.html) in KS
  documentation discuss installation and usage of this runtime
