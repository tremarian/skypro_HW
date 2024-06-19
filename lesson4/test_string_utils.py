import pytest
from string_utils import StringUtils

exemplar = StringUtils()

@pytest.mark.parametrize( 'input_str, result', [
    ('skypro', 'Skypro')
    ])

def capitilize_tests(input_str, result):
    assert exemplar.capitilize(input_str) == result 