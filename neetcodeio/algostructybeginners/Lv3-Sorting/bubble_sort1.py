import random


class Solution:

    def bubble_sort(self, arr: list) -> list:
        for i in range(len(arr) - 1):
            maxi = len(arr) - 1 - i
            for j in range(maxi):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]


sol = Solution()
arr = [4, 3, 2, 1]
sol.bubble_sort(arr)
assert arr == [1, 2, 3, 4]

arr = [10, 1, 20, 2, 30, 3, 4, 40, 5]
sol.bubble_sort(arr)
assert arr == [1, 2, 3, 4, 5, 10, 20, 30, 40]

arr = [0, 4, 3, 2, 4, 0]
sol.bubble_sort(arr)
assert arr == [0, 0, 2, 3, 4, 4]

arr = [1, 3, 5, 4, 2]
sol.bubble_sort(arr)
assert arr == [1, 2, 3, 4, 5]
