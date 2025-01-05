"""
username:   Marlen09
profile:    https://leetcode.com/Marlen09/
time:  O(n) or linear-times
space: O(1) or constant-time
"""


def find_duplicate_number(nums):
    """Using Floyd's Tortoise and Hare algorithm to detect the cycle in the linked list"""
    tortoise = nums[0]
    hare = nums[0]

    # Move tortoise and hare until they meet
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Reset tortoise to the start of the list
    tortoise = nums[0]

    # Move tortoise and hare at the same speed until they meet again
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    # Return the duplicate number
    return tortoise


nums = [1, 3, 4, 2, 2]
# slow_ptr[x]:  1 3 2
# fast_ptr[x]:  1 2 2
print(find_duplicate_number(nums))

nums = [3, 1, 3, 4, 2]
print(find_duplicate_number(nums))
