import pytest
from mpin_checker.part_b import check_strength

dob = "02011998"
anniversary = "05062020"
spouse_dob = "15081995"

def test_strength_common():
    assert check_strength("1234", dob, anniversary, spouse_dob) == "WEAK"

def test_strength_demographic():
    assert check_strength("0201", dob, anniversary, spouse_dob) == "WEAK"

def test_strength_strong():
    assert check_strength("6789", dob, anniversary, spouse_dob) == "STRONG"

def test_invalid_length():
    with pytest.raises(ValueError):
        check_strength("12", dob, anniversary, spouse_dob)
