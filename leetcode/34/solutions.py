def search_range(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    first = None
    last = None

    for index, value in enumerate(nums):
        if value == target:
            if first is None:
                first = index
                last = index
                continue
            last = index
    return [-1, -1] if first is None else [first, last]


# Testing Arena:
assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
assert search_range([], 0) == [-1, -1]
