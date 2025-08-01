# mpin_checker/part_c.py
from .utils import is_common_mpin, get_demographic_mpins

def check_strength_with_reason(mpin: str, dob: str, anniversary: str, spouse_dob: str):
    reasons = []

    demographic_mpins = get_demographic_mpins(dob, anniversary, spouse_dob)

    if is_common_mpin(mpin):
        reasons.append("COMMONLY_USED")
    if dob and mpin in get_demographic_mpins(dob, "", ""):
        reasons.append("DEMOGRAPHIC_DOB_SELF")
    if spouse_dob and mpin in get_demographic_mpins("", "", spouse_dob):
        reasons.append("DEMOGRAPHIC_DOB_SPOUSE")
    if anniversary and mpin in get_demographic_mpins("", anniversary, ""):
        reasons.append("DEMOGRAPHIC_ANNIVERSARY")

    strength = "WEAK" if reasons else "STRONG"
    return {"strength": strength, "reasons": reasons}
