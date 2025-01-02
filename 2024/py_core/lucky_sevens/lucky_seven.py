"""Challenge:
Write a function that takes in an array/list of integers as its paramater:
    - Returns True if there are 3 consecutive integers w
"""

def lucky_sevens(arr):
    if not arr:
        return False

    for i in range(0, len(arr) - 2):
        sum = 0
        for j in range(0, 3):
            sum += arr[i + j]
        if sum == 7:
            return True
    return False

#Test Arena:

assert lucky_sevens([2, 1, 5, 1, 0]) is True  # => 1 + 5 + 1 == 7
assert lucky_sevens([0, -2, 1, 8]) is True  # => -2 + 1 + 8 == 7
assert lucky_sevens([7, 7, 7, 7]) is False
assert lucky_sevens([3, 4, 3, 4]) is False
assert lucky_sevens([]) is False  # => 1 + 5 + 1 == 7
assert lucky_sevens([0]) is False  # => -2 + 1 + 8 == 7
assert lucky_sevens([7, 7]) is False
assert lucky_sevens([3, 4, 0]) is True



