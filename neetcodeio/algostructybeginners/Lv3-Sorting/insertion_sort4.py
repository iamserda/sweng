import random


class Solution:

    def insertionSort(self, arr: list) -> list:
        if len(arr) < 2:
            return arr
        for idx in range(len(arr)):
            jdx = idx - 1
            while jdx >= 0 and arr[jdx] > arr[jdx + 1]:
                arr[jdx], arr[jdx + 1] = arr[jdx + 1], arr[jdx]
                jdx -= 1
        return arr


sol = Solution()

arr = [5, 4, 3, 2, 1]
assert sol.insertionSort(arr) == [1, 2, 3, 4, 5]

# arr = [10, 1, 20, 2, 30, 3, 4, 40, 5]
# assert sol.insertionSort(arr) == [1, 2, 3, 4, 5, 10, 20, 30, 40]

# arr = [0, 4, 3, 2, 4, 0]
# assert sol.insertionSort(arr) == [0, 0, 2, 3, 4, 4]

# arr = [1, 3, 5, 4, 2]
# assert sol.insertionSort(arr) == [1, 2, 3, 4, 5]
