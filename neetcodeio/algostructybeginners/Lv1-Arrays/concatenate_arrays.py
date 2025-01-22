def concate_list(nums: list[int]) -> list[int]:
    if nums:
        return [*nums, *nums]


assert concate_list([1, 2, 3]) == [1, 2, 3, 1, 2, 3]
assert concate_list([1, 3]) == [1, 3, 1, 3]
assert concate_list([1]) != [1, 2]
