import random


class Solution:

    def insertionSort(self, arr: list) -> list:
        """sorts an array of integer values in places, in ascending order"""
        if not arr or len(arr) == 1:
            return arr
        for i in range(1, len(arr)):
            j = i - 1
            while j > -1 and arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j -= 1


sol = Solution()

arr = [10, 1, 20, 2, 30, 3, 4, 40, 5]
sol.insertionSort(arr)
assert arr == [1, 2, 3, 4, 5, 10, 20, 30, 40]
print(arr)

arr = [0, 4, 3, 2, 4, 0]
sol.insertionSort(arr)
assert arr == [0, 0, 2, 3, 4, 4]
print(arr)

arr = [1, 3, 5, 4, 2]
sol.insertionSort(arr)
assert arr == [1, 2, 3, 4, 5]
print(arr)
