def unique_occurrences(arr):
    """Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise."""
    items_and_counts = {}
    for item in arr:
        if item in items_and_counts:
            items_and_counts[item] += 1
            continue
        items_and_counts[item] = 1
    counts_set = set()
    for count in items_and_counts.values():
        if count in counts_set:
            return False
        counts_set.add(count)
    return True


arr = [1, 2, 2, 1, 1, 3]
EXPECTED_OUTPUT = True
assert unique_occurrences(arr) == EXPECTED_OUTPUT, "Failed"

arr = [1, 2]
EXPECTED_OUTPUT = False
assert unique_occurrences(arr) == EXPECTED_OUTPUT, "Failed"

arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
EXPECTED_OUTPUT = True
assert unique_occurrences(arr) == EXPECTED_OUTPUT, "Failed"
