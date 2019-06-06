import pytest  # type: ignore
from fortran_format_converter import convert


def test_integer_format():
    for w in range(1, 81):
        assert convert('I{}'.format(w)) == '{}d'.format(w)
    for d in range(1, 20):
        assert convert('I20.{}'.format(d)) == '20d'
    for d in range(20, 41):
        assert convert('I20.{}'.format(d)) == '020d'
    with pytest.raises(ValueError):
        convert('I')
    with pytest.raises(ValueError):
        convert('I8.4E2')


def test_integer_format_uppercase():
    for w in range(1, 81):
        assert convert('I{}'.format(w), uppercase=True) == '{}d'.format(w)
    for d in range(1, 20):
        assert convert('I20.{}'.format(d), uppercase=True) == '20d'
    for d in range(20, 41):
        assert convert('I20.{}'.format(d), uppercase=True) == '020d'
    with pytest.raises(ValueError):
        convert('I', uppercase=True)
    with pytest.raises(ValueError):
        convert('I8.4E2', uppercase=True)


def test_binary_format():
    for w in range(1, 81):
        assert convert('B{}'.format(w)) == '{}b'.format(w)
    for d in range(1, 20):
        assert convert('B20.{}'.format(d)) == '20b'
    for d in range(20, 41):
        assert convert('B20.{}'.format(d)) == '020b'
    with pytest.raises(ValueError):
        convert('B')
    with pytest.raises(ValueError):
        convert('B8.4E2')


def test_binary_format_uppercase():
    for w in range(1, 81):
        assert convert('B{}'.format(w), uppercase=True) == '{}b'.format(w)
    for d in range(1, 20):
        assert convert('B20.{}'.format(d), uppercase=True) == '20b'
    for d in range(20, 41):
        assert convert('B20.{}'.format(d), uppercase=True) == '020b'
    with pytest.raises(ValueError):
        convert('B', uppercase=True)
    with pytest.raises(ValueError):
        convert('B8.4E2', uppercase=True)


def test_octal_format():
    for w in range(1, 81):
        assert convert('O{}'.format(w)) == '{}o'.format(w)
    for d in range(1, 20):
        assert convert('O20.{}'.format(d)) == '20o'
    for d in range(20, 41):
        assert convert('O20.{}'.format(d)) == '020o'
    with pytest.raises(ValueError):
        convert('O')
    with pytest.raises(ValueError):
        convert('O8.4E2')


def test_octal_format_uppercase():
    for w in range(1, 81):
        assert convert('O{}'.format(w), uppercase=True) == '{}o'.format(w)
    for d in range(1, 20):
        assert convert('O20.{}'.format(d), uppercase=True) == '20o'
    for d in range(20, 41):
        assert convert('O20.{}'.format(d), uppercase=True) == '020o'
    with pytest.raises(ValueError):
        convert('O', uppercase=True)
    with pytest.raises(ValueError):
        convert('O8.4E2', uppercase=True)


def test_hexadecimal_format():
    for w in range(1, 81):
        assert convert('Z{}'.format(w)) == '{}x'.format(w)
    for d in range(1, 20):
        assert convert('Z20.{}'.format(d)) == '20x'
    for d in range(20, 41):
        assert convert('Z20.{}'.format(d)) == '020x'
    with pytest.raises(ValueError):
        convert('Z')
    with pytest.raises(ValueError):
        convert('Z8.4E2')


def test_hexadecimal_format_uppercase():
    for w in range(1, 81):
        assert convert('Z{}'.format(w), uppercase=True) == '{}X'.format(w)
    for d in range(1, 20):
        assert convert('Z20.{}'.format(d), uppercase=True) == '20X'
    for d in range(20, 41):
        assert convert('Z20.{}'.format(d), uppercase=True) == '020X'
    with pytest.raises(ValueError):
        convert('Z', uppercase=True)
    with pytest.raises(ValueError):
        convert('Z8.4E2', uppercase=True)


def test_real_format():
    for d in range(0, 81):
        for w in range(d+1, 81):
            assert convert('F{}.{}'.format(w, d)) == '{}.{}f'.format(w, d)
    with pytest.raises(ValueError):
        convert('F')
    with pytest.raises(ValueError):
        convert('F6')
    with pytest.raises(ValueError):
        convert('F6.2E4')


def test_real_format_uppercase():
    for d in range(0, 81):
        for w in range(d+1, 81):
            assert (convert('F{}.{}'.format(w, d), uppercase=True)
                    == '{}.{}F'.format(w, d))
    with pytest.raises(ValueError):
        convert('F', uppercase=True)
    with pytest.raises(ValueError):
        convert('F6', uppercase=True)
    with pytest.raises(ValueError):
        convert('F6.2E4', uppercase=True)


def test_double_format():
    for d in range(0, 81):
        for w in range(d+1, 81):
            assert convert('D{}.{}'.format(w, d)) == '{}.{}f'.format(w, d)
    with pytest.raises(ValueError):
        convert('D')
    with pytest.raises(ValueError):
        convert('D6')
    with pytest.raises(ValueError):
        convert('D6.2E4')


def test_double_format_uppercase():
    for d in range(0, 81):
        for w in range(d+1, 81):
            assert (convert('D{}.{}'.format(w, d), uppercase=True) ==
                    '{}.{}F'.format(w, d))
    with pytest.raises(ValueError):
        convert('D', uppercase=True)
    with pytest.raises(ValueError):
        convert('D6', uppercase=True)
    with pytest.raises(ValueError):
        convert('D6.2E4', uppercase=True)


def test_exponent_format():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert('E{}.{}'.format(w, d)) == '{}.{}e'.format(w, d)
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('E{}.{}E{}'.format(w, d, e)) ==
                        '{}.{}e'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert convert('E{}.{}D{}'.format(w, d, e)) ==\
                       '{}.{}e'.format(w, d)
    with pytest.raises(ValueError):
        convert('E')
    with pytest.raises(ValueError):
        convert('E6')
    with pytest.raises(ValueError):
        convert('E6.2A4')


def test_exponent_format_uppercase():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert (convert('E{}.{}'.format(w, d), uppercase=True) ==
                    '{}.{}E'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('E{}.{}E{}'.format(w, d, e), uppercase=True) ==
                        '{}.{}E'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('E{}.{}D{}'.format(w, d, e), uppercase=True) ==
                        '{}.{}E'.format(w, d))
    with pytest.raises(ValueError):
        convert('E', uppercase=True)
    with pytest.raises(ValueError):
        convert('E6', uppercase=True)
    with pytest.raises(ValueError):
        convert('E6.2A4', uppercase=True)


def test_engineering_format():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert('EN{}.{}'.format(w, d)) == '{}.{}e'.format(w, d)
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('EN{}.{}E{}'.format(w, d, e)) ==
                        '{}.{}e'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('EN{}.{}D{}'.format(w, d, e)) ==
                        '{}.{}e'.format(w, d))
    with pytest.raises(ValueError):
        convert('EN')
    with pytest.raises(ValueError):
        convert('EN6')
    with pytest.raises(ValueError):
        convert('EN6.2A4')


def test_engineering_format_uppercase():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert (convert('EN{}.{}'.format(w, d), uppercase=True) ==
                    '{}.{}E'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('EN{}.{}E{}'.format(w, d, e), uppercase=True)
                        == '{}.{}E'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('EN{}.{}D{}'.format(w, d, e), uppercase=True)
                        == '{}.{}E'.format(w, d))
    with pytest.raises(ValueError):
        convert('EN', uppercase=True)
    with pytest.raises(ValueError):
        convert('EN6', uppercase=True)
    with pytest.raises(ValueError):
        convert('EN6.2A4', uppercase=True)


def test_scientific_format():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert('ES{}.{}'.format(w, d)) == '{}.{}e'.format(w, d)
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('ES{}.{}E{}'.format(w, d, e)) ==
                        '{}.{}e'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('ES{}.{}D{}'.format(w, d, e)) ==
                        '{}.{}e'.format(w, d))
    with pytest.raises(ValueError):
        convert('ES')
    with pytest.raises(ValueError):
        convert('ES6')
    with pytest.raises(ValueError):
        convert('ES6.2A4')


def test_scientific_format_uppercase():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert (convert('ES{}.{}'.format(w, d), uppercase=True) ==
                    '{}.{}E'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('ES{}.{}E{}'.format(w, d, e), uppercase=True)
                        == '{}.{}E'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('ES{}.{}D{}'.format(w, d, e), uppercase=True)
                        == '{}.{}E'.format(w, d))
    with pytest.raises(ValueError):
        convert('ES', uppercase=True)
    with pytest.raises(ValueError):
        convert('ES6', uppercase=True)
    with pytest.raises(ValueError):
        convert('ES6.2A4', uppercase=True)


def test_logical_format():
    for w in range(0, 81):
        assert convert('L{}'.format(w)) == '{}'.format(w)
    with pytest.raises(ValueError):
        convert('L')
    with pytest.raises(ValueError):
        convert('L4.2')
    with pytest.raises(ValueError):
        convert('L4.2E3')


def test_logical_format_uppercase():
    for w in range(0, 81):
        assert convert('L{}'.format(w), uppercase=True) == '{}'.format(w)
    with pytest.raises(ValueError):
        convert('L', uppercase=True)
    with pytest.raises(ValueError):
        convert('L4.2', uppercase=True)
    with pytest.raises(ValueError):
        convert('L4.2E3', uppercase=True)


def test_string_format():
    assert convert('A') == 's'
    for w in range(0, 81):
        assert convert('A{}'.format(w)) == '{}s'.format(w)
    with pytest.raises(ValueError):
        convert('A4.2')
    with pytest.raises(ValueError):
        convert('A4.2E3')


def test_string_format_uppercase():
    assert convert('A', uppercase=True) == 's'
    for w in range(0, 81):
        assert convert('A{}'.format(w), uppercase=True) == '{}s'.format(w)
    with pytest.raises(ValueError):
        convert('A4.2', uppercase=True)
    with pytest.raises(ValueError):
        convert('A4.2E3', uppercase=True)


def test_general_format():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert convert('G{}.{}'.format(w, d)) == '{}.{}g'.format(w, d)
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('G{}.{}E{}'.format(w, d, e)) ==
                        '{}.{}g'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('G{}.{}D{}'.format(w, d, e)) ==
                        '{}.{}g'.format(w, d))
    with pytest.raises(ValueError):
        convert('G')
    with pytest.raises(ValueError):
        convert('G6')
    with pytest.raises(ValueError):
        convert('G6.2A4')


def test_general_format_uppercase():
    for d in range(0, 21):
        for w in range(d+1, 21):
            assert (convert('G{}.{}'.format(w, d), uppercase=True) ==
                    '{}.{}G'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('G{}.{}E{}'.format(w, d, e), uppercase=True) ==
                        '{}.{}G'.format(w, d))
    for d in range(0, 21):
        for w in range(d+1, 21):
            for e in range(1, 21):
                assert (convert('G{}.{}D{}'.format(w, d, e), uppercase=True) ==
                        '{}.{}G'.format(w, d))
    with pytest.raises(ValueError):
        convert('G', uppercase=True)
    with pytest.raises(ValueError):
        convert('G6', uppercase=True)
    with pytest.raises(ValueError):
        convert('G6.2A4', uppercase=True)


def test_invalid_type():
    with pytest.raises(ValueError):
        convert('Y')
