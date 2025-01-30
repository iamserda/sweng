def remove_duplicates(nums):
    """Given an array, remove duplicated numbers... see readme for more details."""
    replace_index = 0
    for visitor in range(1, len(nums)):
        if nums[visitor - 1] != nums[visitor]:  # is this a new diffent value?
            replace_index += 1
            nums[replace_index] = nums[visitor]
    result = replace_index + 1
    return result


# # Tests Arena:
# remove_duplicates([1, 1, 2])
# remove_duplicates([0, 0, 0, 1, 1, 2, 2, 3, 3, 4])
assert remove_duplicates([1, 1, 2]) == 2
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
