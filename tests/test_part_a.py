import pytest
from mpin_checker.part_a import check_common_mpin

def test_common_mpin_true():
    assert check_common_mpin("1234") == True
    assert check_common_mpin("1111") == True
    assert check_common_mpin("0000") == True

def test_common_mpin_false():
    assert check_common_mpin("5678") == False
    assert check_common_mpin("2468") == False

def test_invalid_length():
    with pytest.raises(ValueError):
        check_common_mpin("123")
