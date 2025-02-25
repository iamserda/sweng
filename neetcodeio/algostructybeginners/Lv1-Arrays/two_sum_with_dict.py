class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        complements = {}
        for index, num in enumerate(nums):
            complements[num] = index
            complement = target - num
            if complement in complements:
                return [complements[complement], index]


arr = [3, 4, 5, 6]
target = 7
sol = Solution()
assert sol.two_sum(arr, target) == [0, 1]  # efficient solution, O(n) time, O(n) space
