import pytest
from string_utils import StringUtils

@pytest.mark.parametrize( 'str, result', [('skypro', 'Skypro')] )

def capitilize_tests(str, result): 
    string = StringUtils()
    res = string.capitilize(str) 
    assert res == result 