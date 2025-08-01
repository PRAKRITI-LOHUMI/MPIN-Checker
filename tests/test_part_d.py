import pytest
from mpin_checker.part_d import check_strength_6digit

dob = "02011998"
anniversary = "05062020"
spouse_dob = "15081995"

def test_common_6digit():
    result = check_strength_6digit("123456", dob, anniversary, spouse_dob)
    assert result["strength"] == "WEAK"
    assert "COMMONLY_USED" in result["reasons"]

def test_demographic_6digit():
    result = check_strength_6digit("020198", dob, anniversary, spouse_dob)
    assert result["strength"] == "WEAK"
    assert "DEMOGRAPHIC_DOB_SELF" in result["reasons"]

def test_strong_6digit():
    result = check_strength_6digit("789654", dob, anniversary, spouse_dob)
    assert result["strength"] == "STRONG"
    assert result["reasons"] == []

def test_invalid_length():
    with pytest.raises(ValueError):
        check_strength_6digit("1234", dob, anniversary, spouse_dob)
