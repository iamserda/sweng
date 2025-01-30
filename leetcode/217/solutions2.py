def contains_duplicates(nums: list[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
    """
    # =================== START HERE ===================
    if not nums:
        return None
    nums_set = set()
    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)
    return False


assert contains_duplicates([1, 2, 3, 4]) is False
assert contains_duplicates([1, 2, 4, 4]) is True
assert contains_duplicates([]) is None
assert contains_duplicates(["1", 1, True, True]) is True
