class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right = len(nums) - 1
        left = right - 1

        while left >= 0:
                if nums[left] == nums[right]:
                    if len(nums) - 1 == right or nums[right + 1] is None:
                        nums[right] = None
                    else:
                        nums[right] = nums[right + 1]
                        nums[right + 1] = None
                left -= 1
                right -= 1
        for i,v in enumerate(nums):
            if v is None:
                return i
            else:
                return len(nums)
