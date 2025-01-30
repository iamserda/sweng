# https://leetcode.com/problems/longest-consecutive-sequence/solutions/41057/simple-o-n-with-explanation-just-walk-each-streak\
def longest_consecutive_sequence(nums):
    """Find the longest sub array that's a consecutive sequence"""
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best

assert longest_consecutive_sequence([-5, 1, 2, 3, 4, -100, 200]) == 4
