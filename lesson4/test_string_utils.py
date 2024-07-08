import pytest
from string_utils import StringUtils

exemplar = StringUtils()


@pytest.mark.parametrize('input_str, result', [
    ('skypro', 'Skypro'),
    ('two words', 'Two words'),
    ('123', '123'),
    ('', ''),
    (' ', ' ')
    ])
def test_capitilize(input_str, result):
    assert exemplar.capitilize(input_str) == result


@pytest.mark.parametrize('input_str, result', [
    (' skypro', 'skypro'),
    ('   skypro', 'skypro'),
    (' two words', 'two words'),
    (' 123', '123'),
    ('', ''),
    (' ', '')
    ])
def test_trim(input_str, result):
    assert exemplar.trim(input_str) == result


@pytest.mark.parametrize('input_str, result', [
    ('a,b,c,d', ['a', 'b', 'c', 'd']),
    ('', []),
    (' ', []),
    ('1,2,3,4', ['1', '2', '3', '4']),
    ('aa,bb,cc,dd', ['aa', 'bb', 'cc', 'dd']),
    ('about something,two words', ['about something', 'two words'])
    ])
def test_to_list(input_str, result):
    assert exemplar.to_list(input_str) == result


@pytest.mark.parametrize('input_str, symbol, result', [
    ('SkyPro', 'S', True),
    ('Two words', 'w', True),
    ('123', '3', True),
    ('Two words', '1', False),
    ('', '', True),
    ('', '123', False),
    (' ', ' ', True),
    ('Two words', ' ', True)
    ])
def test_contains(input_str, symbol, result):
    assert exemplar.contains(input_str, symbol) == result


@pytest.mark.parametrize('input_str, symbol, result', [
    ('SkyPro', 'S', 'kyPro'),
    ('Two words', 'w', 'To ords'),
    ('123', '3', '12'),
    ('Two words', '1', 'Two words'),
    ('', '', ''),
    (' ', ' ', '')
    ])
def test_delete_symbol(input_str, symbol, result):
    assert exemplar.delete_symbol(input_str, symbol) == result


@pytest.mark.parametrize('input_str, symbol, result', [
    ('SkyPro', 'S', True),
    ('Two words', 'T', True),
    ('123', '1', True),
    ('Two words', '1', False),
    ('', '', True),
    ('', '123', False),
    (' ', ' ', True),
    ('Two words', ' ', False)
    ])
def test_starts_with(input_str, symbol, result):
    assert exemplar.starts_with(input_str, symbol) == result


@pytest.mark.parametrize('input_str, symbol, result', [
    ('SkyPro', 'o', True),
    ('Two words', 's', True),
    ('123', '3', True),
    ('Two words', '1', False),
    ('', '', True),
    ('', '123', False),
    (' ', ' ', True),
    ('Two words', ' ', False)
    ])
def test_end_with(input_str, symbol, result):
    assert exemplar.end_with(input_str, symbol) == result


@pytest.mark.parametrize('input_str, result', [
    ('', True),
    (' ', True),
    ('SkyPro', False),
    ('Two words', False),
    ('123', False)
    ])
def test_is_empty(input_str, result):
    assert exemplar.is_empty(input_str) == result


@pytest.mark.parametrize('input_str, result', [
    (['a', 'b', 'c', 'd'], 'a, b, c, d'),
    ([], ''),
    ([' ', ' ',], ' ,  '),
    (['1', '2', '3', '4'], '1, 2, 3, 4'),
    (['aa', 'bb', 'cc', 'dd'], 'aa, bb, cc, dd'),
    (['about something', 'two words'], 'about something, two words')
    ])
def test_list_to_string(input_str, result):
    assert exemplar.list_to_string(input_str) == result
