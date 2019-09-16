Kaitai Struct: runtime library for Python
===========================================

This library implements Kaitai Struct API for Python.

`Kaitai Struct <http://kaitai.io>`_ is a declarative language used for
describe various binary data structures, laid out in files or in memory:
i.e. binary file formats, network stream packet formats, etc.

It is similar to `Python's Construct 2.9 <http://construct.readthedocs.org/>`_ but it is
language-agnostic. The format description is done in YAML-based .ksy
format, which then can be compiled into a wide range of target languages.

Further reading:

* `About Kaitai Struct <http://kaitai.io/>`_
* `About API implemented in this library <http://doc.kaitai.io/stream_api.html>`_
* `Python specific notes <http://doc.kaitai.io/lang_python.html>`_

Installing
------------------------------

Using `requirements.txt`
------------------------------

If you want to use Kaitai Struct runtime in your project and you use
`requirements.txt` to manage your dependencies, just add the following
line to it:

::

    kaitaistruct

and then run `pip install -r requirements.txt` to update all your
dependencies.

Using `pip` directly
------------------------------

You can use

::

    pip install kaitaistruct

to install the package manually using `pip` Python package manager.
