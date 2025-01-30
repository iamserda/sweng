def unique_occurrences(arr):
    """Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise."""


arr = [1, 2, 2, 1, 1, 3]
EXPECTED_OUTPUT = True
assert unique_occurrences(arr) == EXPECTED_OUTPUT, "Failed"

arr = [1, 2]
EXPECTED_OUTPUT = False
assert unique_occurrences(arr) == EXPECTED_OUTPUT, "Failed"

arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
EXPECTED_OUTPUT = True
assert unique_occurrences(arr) == EXPECTED_OUTPUT, "Failed"
