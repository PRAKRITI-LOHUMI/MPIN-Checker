import pytest
from mpin_checker.part_c import check_strength_with_reason

dob = "02011998"
anniversary = "05062020"
spouse_dob = "15081995"

def test_common_mpin_reason():
    result = check_strength_with_reason("1234", dob, anniversary, spouse_dob)
    assert result["strength"] == "WEAK"
    assert "COMMONLY_USED" in result["reasons"]

def test_demographic_reason():
    result = check_strength_with_reason("0201", dob, anniversary, spouse_dob)
    assert "DEMOGRAPHIC_DOB_SELF" in result["reasons"]

def test_strong_mpin():
    result = check_strength_with_reason("6789", dob, anniversary, spouse_dob)
    assert result["strength"] == "STRONG"
    assert result["reasons"] == []
