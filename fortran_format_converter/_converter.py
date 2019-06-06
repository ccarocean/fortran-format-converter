"""Fortran format to Python format string conversion."""

from typing import Tuple, Optional

import regex as re  # type: ignore
from cached_property import cached_property  # type: ignore

__all__ = ['Format', 'convert']

_MATCH_FORMAT = re.compile(
    r'(?|'
    r'(I)(\d+)(?:\.(\d+))?$|'              # integer
    r'([BOZ])(\d+)(?:\.(\d+))?$|'          # binary, octal, and hexadecimal
    r'([FD])(\d+)\.(\d+)$|'                # real and double
    r'(E)(\d+)\.(\d+)(?:[ED](\d+))?$|'     # exponent
    r'(EN)(\d+)\.(\d+)(?:[ED](\d+))?$|'    # engineering
    r'(ES)(\d+)\.(\d+)(?:[ED](\d+))?$|'    # scientific
    r'(L)(\d+)$|'                          # logical
    r'(A)(\d+)?$|'                         # character
    r'(G)(\d+)\.(\d+)(?:[ED](\d+))?$'      # generalized
    r')'
)


class Format:
    """Convert Fortran format specification to Python format string language.

    This conversion is a best effort as the string format options between
    Fortran and Python only share a small subset.  A conversion will always
    be made but it may only loosely resemble the intended result.  This
    incompatibility mainly consists of the following features that Fotran
    supports but Python does not.

        1. Control of field width and 0 padding width separately.  If the
           number of digits is greater than or equal to the field width for
           integers, binary, octal, and hexadecimal zero padding is used for
           the entire width.
        2. Control of the number of exponent digits, Python will always
           choose automatically.
        3. Engineering format.  Exponential format is the fallback.
        4. Scientific format.  Exponential format is the fallback.

    Parameters
    ----------
    fortran_format
        Fortran format specification for a single value as a string.
    uppercase
        Set to True to use uppercase format.  This effects the following:
            1. Hexadecimal digits A-F will be uppercase.
            2. inf and nan will be INF and NAN instead.
            3. The exponent letter will be E instead of e.

    Raises
    ------
    ValueError
        If :paramref:`fortran_format` is not a valid Fortran format
        specification.

    """

    def __init__(self, fortran_format: str, uppercase: bool = False):
        self._uppercase = uppercase
        self._fortran_format = fortran_format
        self._type, self._width, self._digits, self._exponent = (
            self._fortran_parts())

    def _format_error(self) -> Exception:
        return ValueError(
            "'{}' is not a valid Fortran format specifier".format(
                self._fortran_format))

    def _fortran_parts(self) -> \
            Tuple[str, Optional[int], Optional[int], Optional[int]]:
        try:
            type_, width_, digits_, exponent_ = (
                _MATCH_FORMAT.match(self._fortran_format.upper()).groups())
        except AttributeError:
            raise self._format_error()
        width = int(width_) if width_ else None
        digits = int(digits_) if digits_ else None
        exponent = int(exponent_) if exponent_ else None
        return type_, width, digits, exponent

    @cached_property
    def string(self) -> str:
        """Best effort approximating Python format string."""
        align = self.align if self.align != '>' else ''
        sign = self.sign if self.sign != '-' else ''
        width = self.width if self.width is not None else ''
        precision = '.{}'.format(self.precision) \
            if self.precision is not None else ''
        return '{}{}{}{}{}{}'.format(
            self.fill, align, sign, width, precision, self.type)

    @cached_property
    def sign(self) -> str:
        """Sign character."""
        if self.type.lower() in {'d', 'f', 'e', 'g'}:
            return '-'
        return ''

    @property
    def align(self) -> str:
        """Alignment character."""
        return '>'

    @cached_property
    def fill(self) -> str:
        """Fill character."""
        if (self._type in {'I', 'B', 'O', 'Z'} and self._digits and
                self._width and self._digits >= self._width):
            return '0'  # zero fill
        return ''  # space fill

    @cached_property
    def precision(self) -> Optional[int]:
        """Precision for float, exponent, and general, else None."""
        if self.type.lower() in {'f', 'e', 'g'}:
            return self._digits
        return None

    @cached_property
    def type(self) -> str:
        """Type letter."""
        switch = {
            'I': 'd',
            'B': 'b',
            'O': 'o',
            'Z': 'X',
            'F': 'F',
            'E': 'E',
            'D': 'F',
            'EN': 'E',
            'ES': 'E',
            'L': '',
            'A': 's',
            'G': 'G'
        }
        try:
            if self._uppercase:
                return switch[self._type]
            return switch[self._type].lower()
        except KeyError:  # pragma: no cover
            # this can't realy be reached due to the structure of the
            # _MATCH_FORMAT regular expression
            raise self._format_error()

    @property
    def width(self) -> Optional[int]:
        """Width of field."""
        return self._width


def convert(fortran_format: str, uppercase: bool = False) -> str:
    """Convert Fortran format specification to Python format string language.

    See :class:`Format` for more information.

    Parameters
    ----------
    fortran_format
        Fortran format specification for a single value as a string.
    uppercase
        Set to True to use uppercase format.  This effects the following:
            1. Hexadecimal digits A-F will be uppercase.
            2. inf and nan will be INF and NAN instead.
            3. The exponent letter will be E instead of e.

    Returns
    -------
    str
        A Python format string that is a best effort approximation of the
        given :paramref:`fortran_format` string.
    """
    format_string = Format(fortran_format, uppercase).string  # type: str
    return format_string
