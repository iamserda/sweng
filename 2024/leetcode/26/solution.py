def remove_duplicates(nums):
    """Given an array, remove duplicated numbers... see readme for more details."""
    if len(nums) == 0:
        return 0
    prev = 0
    for next in range(1, len(nums)):
        if nums[prev] != nums[next]:
            prev += 1
            nums[prev] = nums[next]
    return prev + 1


# Tests Arena:
assert remove_duplicates([1, 1, 2]) == 2
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
