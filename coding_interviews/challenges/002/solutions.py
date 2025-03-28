"""
Challege:
Most Frequently Occurring Item in an Array (Python)
Find the most frequently occurring item in an array.

Example: The most frequently occurring item in [1, 3, 1, 3, 2, 1] is 1.

If you're given an empty array, you should return null (in Java) or None (in Python).

You can assume that there is always a single, unique value that appears most frequently unless the array is empty.  For instance, you won't be given an array such as [1, 1, 2, 2].

NOTE: We're going to use lists instead of arrays in Python for simplicity.
"""


# Implement your function below.
def most_frequent(given_list):
    if not given_list:
        return None
    max_item = float("-inf")
    max_count = float("-inf")
    dictio = {}
    for item in given_list:
        if item in dictio:
            dictio[item] += 1
        else:
            dictio[item] = 1
    for num, count in dictio.items():
        if count >= max_count:
            max_item, max_count = num, count

    return max_item


# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
assert most_frequent([1, 3, 1, 3, 2, 1]) == 1

# most_frequent(list2) should return 3
assert most_frequent([3, 3, 1, 3, 2, 1]) == 3

# most_frequent(list3) should return None
assert most_frequent([]) == None

# most_frequent(list4) should return 0
assert most_frequent([0]) == 0

# most_frequent(list5) should return -1
assert most_frequent([0, -1, 10, 10, -1, 10, -1, -1, -1, 1]) == -1
