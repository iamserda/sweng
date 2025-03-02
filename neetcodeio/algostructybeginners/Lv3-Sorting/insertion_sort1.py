import random


class Solution:

    def insertionSort(self, arr: list) -> list:
        # time complexity: 0(n**2)
        # space complexity: O(1)
        if not arr or len(arr) <= 1:
            return arr

        for index in range(1, len(arr)):
            jndex = index - 1  # to compare it to the next item to its right.
            while jndex >= 0 and arr[jndex + 1] < arr[jndex]:
                arr[jndex + 1], arr[jndex] = arr[jndex], arr[jndex + 1]
                jndex -= 1
        return arr


# TESTING ARENA:
sol = Solution()

arr = [10, 1, 20, 2, 30, 3, 4, 40, 5]
sorted_arr = sorted(arr)
assert sol.insertionSort(arr) == sorted_arr

arr = [0, 4, 3, 2, 4, 0]
sorted_arr = sorted(arr)
assert sol.insertionSort(arr) == sorted_arr

arr = [1, 3, 5, 4, 2]
sorted_arr = sorted(arr)
assert sol.insertionSort(arr) == sorted_arr

arr = []
sorted_arr = sorted(arr)
assert sol.insertionSort(arr) == sorted_arr

arr = [3]
sorted_arr = sorted(arr)
assert sol.insertionSort(arr) == sorted_arr
# Walkthrough:
# i=1, j=0
# [4, 3, 2, 1] => [3, 4, 2, 1]
# i=1, j=-1
# [3, 4, 2, 1]

# i=2, j=1
# [3, 4, 2, 1] => [3, 2, 4, 1]
# i=2, j=0
# [3, 2, 4, 1] => [2, 3, 4, 1]
# i=2, j=-1
# [2, 3, 4, 1]

# i=3, j=2
# [2, 3, 4, 1] => [2, 3, 1, 4]
# i=3, j=1
# [2, 3, 1, 4] => [2, 1, 3, 4]
# i=3, j=0
# [2, 1, 3, 4] => [1, 2, 3, 4]
# i=4, out of bound, for loop terminates
