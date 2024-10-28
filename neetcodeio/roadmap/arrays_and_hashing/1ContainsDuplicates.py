class Solution:
    def hasDuplicateNaive(self, nums: list[int]) -> bool:
        for idx in range(0, len(nums)-1):
            for jdx in range(idx+1, len(nums)):
                if nums[idx] == nums[jdx]:
                    return True
                continue
        return False

    def has_duplicate_sorting(self, nums: list[int]) -> bool:
        nums.sort() # sort in-place
        for idx in range(1, len(nums)):
            if nums[idx - 1] == nums[idx]:
                return True
        return False

    def has_duplicate_using_set(self, nums: list[int]) -> bool:
        my_set = set()
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
        return False


#Testing Arenas:
sol = Solution()
assert sol.hasDuplicateNaive([1,2,3,3]) is True
assert sol.hasDuplicateNaive([1,2,3,4]) is False

assert sol.has_duplicate_sorting([1,2,3,3]) is True
assert sol.has_duplicate_sorting([1,2,3,4]) is False

assert sol.has_duplicate_using_set([1,2,3,3]) is True
assert sol.has_duplicate_using_set([1,2,3,4]) is False