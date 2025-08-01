# mpin_checker/part_d.py
from .utils import is_common_mpin, get_demographic_mpins

def check_strength_6digit(mpin: str, dob: str, anniversary: str, spouse_dob: str):
    if len(mpin) != 6:
        raise ValueError("MPIN must be 6 digits for Part D")

    reasons = []
    demographic_mpins = get_demographic_mpins(dob, anniversary, spouse_dob)

    if is_common_mpin(mpin):
        reasons.append("COMMONLY_USED")
    if dob and mpin in demographic_mpins:
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if spouse_dob and mpin in demographic_mpins:
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if anniversary and mpin in demographic_mpins:
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    strength = "WEAK" if reasons else "STRONG"
    return {"strength": strength, "reasons": reasons}
