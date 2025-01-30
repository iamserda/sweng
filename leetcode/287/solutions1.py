"""TC: O(n), SC: O(n)"""


def find_duplicate_number(nums):
    """Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive."""
    nums_hashtable = set()
    for num in nums:
        if num in nums_hashtable:
            return num
        nums_hashtable.add(num)
    return None


nums = [1, 3, 4, 2, 2]
print(find_duplicate_number(nums))
nums = [3, 1, 3, 4, 2]
print(find_duplicate_number(nums))
