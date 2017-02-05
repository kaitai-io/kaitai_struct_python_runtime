from setuptools import setup
from io import open

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kaitaistruct',
    version='0.6',
    description='Kaitai Struct declarative parser generator for binary data: runtime library for Python',
    long_description=long_description,
    url='http://kaitai.io',
    author='Kaitai Project',
    author_email='greycat@kaitai.io',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='kaitai,struct,ksy,declarative,data structure,data format,file format,packet format,binary,parser,parsing,unpack,development',
    py_modules=["kaitaistruct"]
)
