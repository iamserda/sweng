# SCRATCH SOLUTION 1
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums:
            arr = [0] * len(set(nums))
            for num in nums:
                arr[num] += 1
            # [2, 2, 2]
            nums_index = 0
            for arr_index in range(len(arr)):
                for _ in range(arr[arr_index]):
                    nums[nums_index] = arr_index
                    nums_index += 1
        return nums


sol = Solution()
print(sol.sortColors([2, 0, 2, 1, 1, 0]))
