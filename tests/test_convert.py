import pytest  # type: ignore
from fortran_format_converter import convert


def test_integer_format():
    for w in range(1, 81):
        assert convert(f'I{w}') == f'{w}d'
    for d in range(1, 20):
        assert convert(f'I20.{d}') == '20d'
    for d in range(20, 41):
        assert convert(f'I20.{d}') == '020d'
    with pytest.raises(ValueError):
        convert('I')
    with pytest.raises(ValueError):
        convert('I8.4E2')


def test_integer_format_uppercase():
    for w in range(1, 81):
        assert convert(f'I{w}', uppercase=True) == f'{w}d'
    for d in range(1, 20):
        assert convert(f'I20.{d}', uppercase=True) == '20d'
    for d in range(20, 41):
        assert convert(f'I20.{d}', uppercase=True) == '020d'
    with pytest.raises(ValueError):
        convert('I', uppercase=True)
    with pytest.raises(ValueError):
        convert('I8.4E2', uppercase=True)


def test_binary_format():
    for w in range(1, 81):
        assert convert(f'B{w}') == f'{w}b'
    for d in range(1, 20):
        assert convert(f'B20.{d}') == f'20b'
    for d in range(20, 41):
        assert convert(f'B20.{d}') == f'020b'
    with pytest.raises(ValueError):
        convert('B')
    with pytest.raises(ValueError):
        convert('B8.4E2')


def test_binary_format_uppercase():
    for w in range(1, 81):
        assert convert(f'B{w}', uppercase=True) == f'{w}b'
    for d in range(1, 20):
        assert convert(f'B20.{d}', uppercase=True) == f'20b'
    for d in range(20, 41):
        assert convert(f'B20.{d}', uppercase=True) == f'020b'
    with pytest.raises(ValueError):
        convert('B', uppercase=True)
    with pytest.raises(ValueError):
        convert('B8.4E2', uppercase=True)


def test_octal_format():
    for w in range(1, 81):
        assert convert(f'O{w}') == f'{w}o'
    for d in range(1, 20):
        assert convert(f'O20.{d}') == f'20o'
    for d in range(20, 41):
        assert convert(f'O20.{d}') == f'020o'
    with pytest.raises(ValueError):
        convert('O')
    with pytest.raises(ValueError):
        convert('O8.4E2')


def test_octal_format_uppercase():
    for w in range(1, 81):
        assert convert(f'O{w}', uppercase=True) == f'{w}o'
    for d in range(1, 20):
        assert convert(f'O20.{d}', uppercase=True) == f'20o'
    for d in range(20, 41):
        assert convert(f'O20.{d}', uppercase=True) == f'020o'
    with pytest.raises(ValueError):
        convert('O', uppercase=True)
    with pytest.raises(ValueError):
        convert('O8.4E2', uppercase=True)


def test_hexadecimal_format():
    for w in range(1, 81):
        assert convert(f'Z{w}') == f'{w}x'
    for d in range(1, 20):
        assert convert(f'Z20.{d}') == f'20x'
    for d in range(20, 41):
        assert convert(f'Z20.{d}') == f'020x'
    with pytest.raises(ValueError):
        convert('Z')
    with pytest.raises(ValueError):
        convert('Z8.4E2')


def test_hexadecimal_format_uppercase():
    for w in range(1, 81):
        assert convert(f'Z{w}', uppercase=True) == f'{w}X'
    for d in range(1, 20):
        assert convert(f'Z20.{d}', uppercase=True) == f'20X'
    for d in range(20, 41):
        assert convert(f'Z20.{d}', uppercase=True) == f'020X'
    with pytest.raises(ValueError):
        convert('Z', uppercase=True)
    with pytest.raises(ValueError):
        convert('Z8.4E2', uppercase=True)


def test_real_format():
    for d in range(0, 81):
        for w in range(d+1, 81):
            assert convert(f'F{w}.{d}') == f'{w}.{d}f'
    with pytest.raises(ValueError):
        convert('F')
    with pytest.raises(ValueError):
        convert('F6')
    with pytest.raises(ValueError):
        convert('F6.2E4')


def test_real_format_uppercase():
    for d in range(0, 81):
        for w in range(d+1, 81):
            assert convert(f'F{w}.{d}', uppercase=True) == f'{w}.{d}F'
    with pytest.raises(ValueError):
        convert('F', uppercase=True)
    with pytest.raises(ValueError):
        convert('F6', uppercase=True)
    with pytest.raises(ValueError):
        convert('F6.2E4', uppercase=True)


def test_double_format():
    for d in range(0, 81):
        for w in range(d+1, 81):
            assert convert(f'D{w}.{d}') == f'{w}.{d}f'
    with pytest.raises(ValueError):
        convert('D')
    with pytest.raises(ValueError):
        convert('D6')
    with pytest.raises(ValueError):
        convert('D6.2E4')


def test_double_format_uppercase():
    for d in range(0, 81):
        for w in range(d+1, 81):
            assert convert(f'D{w}.{d}', uppercase=True) == f'{w}.{d}F'
    with pytest.raises(ValueError):
        convert('D', uppercase=True)
    with pytest.raises(ValueError):
        convert('D6', uppercase=True)
    with pytest.raises(ValueError):
        convert('D6.2E4', uppercase=True)


def test_exponent_format():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert(f'E{w}.{d}') == f'{w}.{d}e'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'E{w}.{d}E{e}') == f'{w}.{d}e'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'E{w}.{d}D{e}') == f'{w}.{d}e'
    with pytest.raises(ValueError):
        convert('E')
    with pytest.raises(ValueError):
        convert('E6')
    with pytest.raises(ValueError):
        convert('E6.2A4')


def test_exponent_format_uppercase():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert(f'E{w}.{d}', uppercase=True) == f'{w}.{d}E'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'E{w}.{d}E{e}', uppercase=True) == f'{w}.{d}E'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'E{w}.{d}D{e}', uppercase=True) == f'{w}.{d}E'
    with pytest.raises(ValueError):
        convert('E', uppercase=True)
    with pytest.raises(ValueError):
        convert('E6', uppercase=True)
    with pytest.raises(ValueError):
        convert('E6.2A4', uppercase=True)


def test_engineering_format():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert(f'EN{w}.{d}') == f'{w}.{d}e'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'EN{w}.{d}E{e}') == f'{w}.{d}e'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'EN{w}.{d}D{e}') == f'{w}.{d}e'
    with pytest.raises(ValueError):
        convert('EN')
    with pytest.raises(ValueError):
        convert('EN6')
    with pytest.raises(ValueError):
        convert('EN6.2A4')


def test_engineering_format_uppercase():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert(f'EN{w}.{d}', uppercase=True) == f'{w}.{d}E'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'EN{w}.{d}E{e}', uppercase=True) == f'{w}.{d}E'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'EN{w}.{d}D{e}', uppercase=True) == f'{w}.{d}E'
    with pytest.raises(ValueError):
        convert('EN', uppercase=True)
    with pytest.raises(ValueError):
        convert('EN6', uppercase=True)
    with pytest.raises(ValueError):
        convert('EN6.2A4', uppercase=True)


def test_scientific_format():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert(f'ES{w}.{d}') == f'{w}.{d}e'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'ES{w}.{d}E{e}') == f'{w}.{d}e'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'ES{w}.{d}D{e}') == f'{w}.{d}e'
    with pytest.raises(ValueError):
        convert('ES')
    with pytest.raises(ValueError):
        convert('ES6')
    with pytest.raises(ValueError):
        convert('ES6.2A4')


def test_scientific_format_uppercase():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert(f'ES{w}.{d}', uppercase=True) == f'{w}.{d}E'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'ES{w}.{d}E{e}', uppercase=True) == f'{w}.{d}E'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'ES{w}.{d}D{e}', uppercase=True) == f'{w}.{d}E'
    with pytest.raises(ValueError):
        convert('ES', uppercase=True)
    with pytest.raises(ValueError):
        convert('ES6', uppercase=True)
    with pytest.raises(ValueError):
        convert('ES6.2A4', uppercase=True)


def test_logical_format():
    for w in range(0, 81):
        assert convert(f'L{w}') == f'{w}'
    with pytest.raises(ValueError):
        convert('L')
    with pytest.raises(ValueError):
        convert('L4.2')
    with pytest.raises(ValueError):
        convert('L4.2E3')


def test_logical_format_uppercase():
    for w in range(0, 81):
        assert convert(f'L{w}') == f'{w}'
    with pytest.raises(ValueError):
        convert('L')
    with pytest.raises(ValueError):
        convert('L4.2')
    with pytest.raises(ValueError):
        convert('L4.2E3')


def test_string_format():
    assert convert('A') == f's'
    for w in range(0, 81):
        assert convert(f'A{w}') == f'{w}s'
    with pytest.raises(ValueError):
        convert('A4.2')
    with pytest.raises(ValueError):
        convert('A4.2E3')


def test_string_format_uppercase():
    assert convert('A', uppercase=True) == f's'
    for w in range(0, 81):
        assert convert(f'A{w}', uppercase=True) == f'{w}s'
    with pytest.raises(ValueError):
        convert('A4.2', uppercase=True)
    with pytest.raises(ValueError):
        convert('A4.2E3', uppercase=True)


def test_general_format():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert(f'G{w}.{d}') == f'{w}.{d}g'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'G{w}.{d}E{e}') == f'{w}.{d}g'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'G{w}.{d}D{e}') == f'{w}.{d}g'
    with pytest.raises(ValueError):
        convert('G')
    with pytest.raises(ValueError):
        convert('G6')
    with pytest.raises(ValueError):
        convert('G6.2A4')


def test_general_format_uppercase():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert(f'G{w}.{d}', uppercase=True) == f'{w}.{d}G'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'G{w}.{d}E{e}', uppercase=True) == f'{w}.{d}G'
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert(f'G{w}.{d}D{e}', uppercase=True) == f'{w}.{d}G'
    with pytest.raises(ValueError):
        convert('G', uppercase=True)
    with pytest.raises(ValueError):
        convert('G6', uppercase=True)
    with pytest.raises(ValueError):
        convert('G6.2A4', uppercase=True)


def test_invalid_type():
    with pytest.raises(ValueError):
        convert('Y')
