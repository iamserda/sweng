import random


class Solution:

    def insertionSort(self, arr: list) -> list:
        for index in range(1, len(arr)):
            jndex = index - 1
            while jndex >= 0 and arr[jndex + 1] < arr[jndex]:
                arr[jndex + 1], arr[jndex] = arr[jndex], arr[jndex + 1]
                jndex -= 1
        return arr


sol = Solution()

arr = [10, 1, 20, 2, 30, 3, 4, 40, 5]
assert sol.insertionSort(arr) == [1, 2, 3, 4, 5, 10, 20, 30, 40]

arr = [0, 4, 3, 2, 4, 0]
assert sol.insertionSort(arr) == [0, 0, 2, 3, 4, 4]

arr = [1, 3, 5, 4, 2]
assert sol.insertionSort(arr) == [1, 2, 3, 4, 5]
