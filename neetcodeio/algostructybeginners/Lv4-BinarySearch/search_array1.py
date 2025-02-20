import math


class Solution:
    def binary_search(self, arr, val):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = int(math.ceil((right - left) // 2))
            if arr[mid] == val:
                return mid
            if val > arr[mid]:
                


arr = [i for i in range(1, 101)]
sol = Solution()
sol.binary_search(arr, val)
