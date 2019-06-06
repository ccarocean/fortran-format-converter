fortran-format-converter
========================

Convert Fortran format specifiers to Python format strings.

|build-status|
|coverage-status|

|version|
|supported-versions|
|wheel|
|status|



Requirements
------------

* Python 3.5 or greater
* regex_
* cached-property_



Installation
------------

`fortran-format-converter` is on PyPI_ so the easiest way to install it is:

.. code-block:: text

    $ pip install fortran-format-converter



Usage
-----

Currently `fortran-format-converter` only handles simple conversions and in a
single direction, Fortan -> Python.


We begin by importing the converter.

.. code-block:: python

    import fortran_format_converter as ffc

Now to convert a Fortran style format specification to a Python format
string is as simple as supplying the `convert` function with the Fortran
formatting specification.

.. code-block:: python

    >>> ffc.convert('F6.2')
    '6.2f'

Most types of Fortran format specifications are supported, such as binary.

.. code-block:: python

    >>> ffc.convert('B16.16')
    '016b'

If an invalid format string is given an error will be raised.

.. code-block:: python

    >>> ffc.convert('J4')
    Traceback (most recent call last):
    ...
    ValueError: 'J4' is not a valid Fortran format specifier

Sometimes it may be desirable to parameterized the format.  This can be
accomplished with the `width`, `align`, and `precision` fields of the
`Format` class.

.. code-block:: python

    >>> format = ffc.Format('F5.2')
    >>> '{:{width}.{prec}f}'.format(2.718281828459, width=format.width, prec=format.precision)
     2.72

.. note::

    `fortran-format-converter` is a best effort converter, many Fortran format
    strings are not convertible to Python format strings.  When the format is
    not compatible a similar but not necessarily identical format will be used.

    If Fortran identical formatting is desired you should look into the
    excellent fortranformat_ package by *Brendan Arnold* which reads or writes
    directly without translation through Python format strings.
    `fortran-format-converter` is intended for applications where a Python
    compatible format string (and not the result) is required, such as for
    matplotlib_ tick formatting.


.. _PyPI: https://pypi.org/
.. _fortranformat: https://bitbucket.org/brendanarnold/py-fortranformat/src
.. _matplotlib: https://matplotlib.org/
.. _regex: https://bitbucket.org/mrabarnett/mrab-regex
.. _cached-property: https://github.com/pydanny/cached-property

.. |build-status| image:: https://travis-ci.com/ccarocean/fortran-format-converter.svg?branch=master&style=flat
   :target: https://travis-ci.com/ccarocean/fortran-format-converter
   :alt: Build status

.. |coverage-status| image:: http://codecov.io/gh/ccarocean/fortran-format-converter/coverage.svg?branch=master
   :target: http://codecov.io/gh/ccarocean/fortran-format-converter?branch=master
   :alt: Test coverage

.. |version| image:: https://img.shields.io/pypi/v/fortran-format-converter.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/fortran-format-converter

.. |status| image:: https://img.shields.io/pypi/status/fortran-format-converter.svg
    :alt: Status
    :target: https://pypi.python.org/pypi/fortran-format-converter

.. |wheel| image:: https://img.shields.io/pypi/wheel/fortran-format-converter.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/fortran-format-converter

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/fortran-format-converter.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/fortran-format-converter

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/fortran-format-converter.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/fortran-format-converter
