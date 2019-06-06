import os
import re
from setuptools import setup, find_packages


def read_version(filename):
    return re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        read(filename), re.MULTILINE).group(1)


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as infile:
        text = infile.read()
    return text


setup(
    name='fortran-format-converter',
    version=read_version('fortran_format_converter/__init__.py'),
    author='Michael R. Shannon',
    author_email='mrshannon.aerospace@gmail.com',
    description='Convert Fortran format specifiers to Python format strings.',
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    license='MIT',
    url='https://github.com/ccarocean/fortran-format-converter',
    packages=find_packages(),
    package_data={
        'fortran-format-converter': ['py.typed']
    },
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering'
    ],
    zip_safe=False
)
