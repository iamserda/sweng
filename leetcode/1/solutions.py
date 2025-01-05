def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    complements = {}
    for index, value in enumerate(nums):
        complement = target - value
        if complement in complements:
            return [complements[complement], index]
        complements[value] = index


assert two_sum([2, 3, 4, 8, 10], 14) == [2, 4] or [4, 2]
assert two_sum([2, 7, 11, 15], 9) == [0, 1] or [1, 0]
assert two_sum([3, 2, 4], 6) == [1, 2] or [2, 1]
assert two_sum([3, 3], 6) == [0, 1] or [1, 0]
assert two_sum([], 14) is None
