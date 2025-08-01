# mpin_checker/part_b.py
from .utils import is_common_mpin, get_demographic_mpins

def check_strength(mpin: str, dob: str, anniversary: str, spouse_dob: str) -> str:
    if len(mpin) != 4:
        raise ValueError("MPIN must be 4 digits for Part B")

    demographic_mpins = get_demographic_mpins(dob, anniversary, spouse_dob)

    if is_common_mpin(mpin) or mpin in demographic_mpins:
        return "WEAK"
    return "STRONG"
