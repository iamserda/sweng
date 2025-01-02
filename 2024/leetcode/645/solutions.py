def find_error_nums(nums):
    """You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.You are given an integer array nums representing the data status of this set after the error. Find the number that occurs twice and the number that is missing and return them in the form of an array."""

    if len(nums) < 2:
        return nums
    nums.sort()
    for i, v in enumerate(nums):
        if i + 1 == len(nums):
            return []
        if v == nums[i + 1]:
            dup_found = v
            break
    set1 = set(i for i in range(1, len(nums) + 1))
    set2 = set(nums)
    item = list(set1.difference(set2))[0]
    return [dup_found, item]


# TESTS ARENA
nums1 = [1, 2, 2, 4]
assert find_error_nums(nums1) == [2, 3]
nums1 = [1, 1]
assert find_error_nums(nums1) == [1, 2]
