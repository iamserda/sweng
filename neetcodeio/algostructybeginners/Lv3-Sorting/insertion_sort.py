import random


class Solution:
    def insertionSort(self, pairs: list) -> list:
        for index in range(len(pairs)):
            jndex = index
            while jndex > 0 and pairs[jndex] < pairs[jndex - 1]:
                pairs[jndex], pairs[jndex - 1] = pairs[jndex - 1], pairs[jndex]
                jndex -= 1
        return pairs


sol1 = Solution()
arr = [5, 4, 3, 2, 1, 0]
assert sol1.insertionSort(arr) == [0, 1, 2, 3, 4, 5]
arr = [0, 4, 3, 2, 4, 0]
assert sol1.insertionSort(arr) == [0, 0, 2, 3, 4, 4]
arr = [0, 1, 3, 5, 4, 2]
assert sol1.insertionSort(arr) == [0, 1, 2, 3, 4, 5]
