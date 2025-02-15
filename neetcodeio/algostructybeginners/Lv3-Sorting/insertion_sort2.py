import random


class Solution:

    def insertionSort(self, arr: list) -> list:
        if len(arr) < 2:
            return arr
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0 and arr[j] > arr[j+1]:

                
sol = Solution()

arr = [10, 1, 20, 2, 30, 3, 4, 40, 5]
assert sol.insertionSort(arr) == [1, 2, 3, 4, 5, 10, 20, 30, 40]

arr = [0, 4, 3, 2, 4, 0]
assert sol.insertionSort(arr) == [0, 0, 2, 3, 4, 4]

arr = [1, 3, 5, 4, 2]
assert sol.insertionSort(arr) == [1, 2, 3, 4, 5]
