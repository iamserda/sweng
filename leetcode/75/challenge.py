class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass


sol = Solution()
assert sol.sortColors(nums=[1, 0, 1, 2]) == [0, 1, 1, 2]
assert sol.sortColors(nums=[2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
assert sol.sortColors(nums=[2, 1, 0]) == [0, 1, 2]
