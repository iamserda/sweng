"""
Challenge:
Write a function that takes in an array, and a number:
- Returns True if 3 contiguous integers within the array/list adds up to the number.
- Returns False for all other cases.
"""
def lucky_num(arr:list, num:int)->bool:
    if not arr:
        return False

    for i in range(0, len(arr) - 2):
        sum = 0
        for j in range(0, 3):
            sum += arr[i + j]
        if sum == num:
            return True
    return False

#Test Arena:

assert lucky_num([2, 1, 5, 1, 0], 7) is True  # => 1 + 5 + 1 == 7
assert lucky_num([0, -2, 1, 8],7) is True  # => -2 + 1 + 8 == 7
assert lucky_num([7, 7, 7, 7], 10) is False
assert lucky_num([3, 4, 3, 4], 12) is False
assert lucky_num([], 0) is False  # => 1 + 5 + 1 == 7
assert lucky_num([0], 0) is False  # => -2 + 1 + 8 == 7
assert lucky_num([7, 7], 14) is False
assert lucky_num([3, 4, 0], 7) is True