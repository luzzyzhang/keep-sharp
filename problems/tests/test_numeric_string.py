
import pytest

from problems.p36_numberic_string import is_numeric, isnumeric


test_params = [
    ("100", True), ("123.45e+6", True), ("+500", True), ("5e2", True),
    ("3.1416", True), ("600.", True), ("-.123", True), ("-1E-16", True),
    ("1.79769313486232E+308", True), ("12e", False), ("1a3.14", False),
    ("1+23", False), ("1.2.3", False), ("+-5", False), ("12e+5.4", False),
    (".", False), (".e1", False), ("e1", False), ("+.", False), ("", False),
]


@pytest.mark.parametrize('string, expected', test_params)
def test_is_numeric_string(string, expected):
    assert isnumeric(string) == expected
    assert is_numeric(string) == expected
