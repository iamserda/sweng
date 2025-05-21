class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_arr = [0] * len(set(nums))
        for num in nums:
            count_arr[num] += 1

        nums_index = 0
        for count_arr_index in range(len(count_arr)):
            for _ in range(count_arr[count_arr_index]):
                nums[nums_index] = count_arr_index
                nums_index += 1


sol = Solution()
nums = [1, 0, 1, 2]
sol.sortColors(nums)
assert nums == [0, 1, 1, 2]

nums = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums)
assert nums == [0, 0, 1, 1, 2, 2]

nums = [2, 1, 0]
sol.sortColors(nums)
assert nums == [0, 1, 2]
