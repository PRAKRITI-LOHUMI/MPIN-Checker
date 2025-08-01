# mpin_checker/part_a.py
from .utils import is_common_mpin

def check_common_mpin(mpin: str) -> bool:
    if len(mpin) != 4:
        raise ValueError("MPIN must be 4 digits for Part A")
    return is_common_mpin(mpin)
