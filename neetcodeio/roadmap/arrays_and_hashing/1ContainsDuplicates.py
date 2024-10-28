class Solution:
    def hasDuplicateNaive(self, nums: list[int]) -> bool:
        for idx in range(0, len(nums)-1):
            for jdx in range(idx+1, len(nums)):
                if nums[idx] == nums[jdx]:
                    return True
                continue
        return False

#Testing Arenas:
sol = Solution()
assert sol.hasDuplicateNaive([1,2,3,3]) is True
assert sol.hasDuplicateNaive([1,2,3,4]) is False
