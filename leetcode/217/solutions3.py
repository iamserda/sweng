def contains_duplicates(nums: list[int]) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
    """
    # =================== START HERE ===================
    if not nums:
        return None
    nums.sort()
    i = 0  # indexer
    size = len(nums)
    while i < (size - 1):
        if nums[i] == nums[i + 1]:
            return True
        i += 1
    return False


assert contains_duplicates([1, 2, 3, 4]) is False
assert contains_duplicates([1, 2, 4, 4]) is True
assert contains_duplicates([]) is None
# assert contains_duplicates(["1", 1, True, True]) is True
