class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


# TESTING ARENA
sol = Solution()
assert sol.hasDuplicate([1, 2, 3, 3]) == True
assert sol.hasDuplicate([1, 2, 4, 3]) == False
