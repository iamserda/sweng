class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
        return [-1, -1]


arr = [3, 4, 5, 6]
target = 7
sol = Solution()
assert sol.twoSum(arr, target) == [0, 1]
