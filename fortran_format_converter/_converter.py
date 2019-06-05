from typing import Tuple, Optional

import regex as re
from cached_property import cached_property


_MATCH_FORMAT = re.compile(
    r'(?|'
    r'(I)(\d+)(?:\.(\d+))?$|'              # integer
    r'([BOZ])(\d+)(?:\.(\d+))?$|'          # binary, octal, and hexadecimal
    r'([FD])(\d+)\.(\d+)$|'                # real and double
    r'(E)(\d+)\.(\d+)(?:[ED](\d+))?$|'     # exponent
    r'(EN)(\d+)\.(\d+)(?:[ED](\d+))?$|'    # engineering
    r'(ES)(\d+)\.(\d+)(?:[ED](\d+))?$|'    # scientific
    r'(L)(\d+)$|'                          # logical
    r'(A)(\d+)$|'                          # character
    r'(G)(\d+)\.(\d+)(?:[ED](\d+))?$'      # generalized
    r')'
)


class Format:

    def __init__(self, fortran_format: str, uppercase: bool = False):
        self._uppercase = uppercase
        self._fortran_format = fortran_format
        self._type, self._width, self._digits, self._exponent = (
            self._fortran_parts())

    def _format_error(self) -> Exception:
        return ValueError(
            f"'{self._fortran_format}' is not a valid "
            "Fortran format specifier")

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
    def string(self):
        align = self.align if self.align != '>' else ''
        sign = self.align if self.sign != '-' else ''
        precision = f'.{self.precision}' if self.precision else ''
        return f'{self.fill}{align}{sign}{self.width}{precision}{self.type}'

    @cached_property
    def sign(self) -> str:
        if self.type.lower() in {'d', 'f', 'e', 'g'}:
            return '-'
        return ''

    @property
    def align(self):
        return '>'

    @cached_property
    def fill(self) -> str:
        if (self._type in {'I', 'B', 'O', 'Z'} and self._digits and
                self._width and self._digits >= self._width):
            return '0'  # zero fill
        return ''  # space fill

    @cached_property
    def precision(self) -> Optional[int]:
        if self.type.lower() in {'f', 'e', 'g'}:
            return self._digits
        return None

    @cached_property
    def type(self) -> str:
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
            else:
                return switch[self._type].lower()
        except KeyError:
            raise self._format_error()

    @property
    def width(self):
        return self._width


def convert(fortran_format: str, uppercase: bool = False) -> str:
    return Format(fortran_format, uppercase).string
