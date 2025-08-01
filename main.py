from mpin_checker.part_a import check_common_mpin
from mpin_checker.part_b import check_strength
from mpin_checker.part_c import check_strength_with_reason
from mpin_checker.part_d import check_strength_6digit

if __name__ == "__main__":
    dob = "02011998"
    anniversary = "05062020"
    spouse_dob = "15081995"

    # mpin = "0201"
    mpin = input()

    print("Part A:", check_common_mpin(mpin))
    print("Part B:", check_strength(mpin, dob, anniversary, spouse_dob))
    print("Part C:", check_strength_with_reason(mpin, dob, anniversary, spouse_dob))
    print("Part D:", check_strength_6digit("020198", dob, anniversary, spouse_dob))
