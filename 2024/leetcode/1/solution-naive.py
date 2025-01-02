def two_sum(nums: list, target: int)->None:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # naive:
    results = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                results = [i, j]
                return results

assert two_sum([2, 3, 4, 8, 10], 14) == [4, 2] or [2, 4]
assert two_sum([2, 7, 11, 15], 9) == [0, 1] or [1, 0]
assert two_sum([3, 2, 4], 6) == [1, 2] or [2, 1]
assert two_sum([3, 3], 6) == [0, 1] or [1, 0]
assert two_sum([], 14) is None