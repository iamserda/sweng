import math



class Solution:
    def binary_search(self, arr, val):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (right + left) // 2
            if val > arr[mid]:
                left = mid + 1
            elif val < arr[mid]:
                right = mid - 1
            else:
                return mid
        return -1


arr = [i for i in range(-100, 100)]
sol = Solution()
index = sol.binary_search(arr, 10)
assert sol.binary_search(arr, val=10) != -1  # Found
index = sol.binary_search(arr, 400)
assert sol.binary_search(arr, val=400) == -1  # Not Found
