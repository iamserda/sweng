class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        pass


sol = Solution()
candidates = [2, 3, 6, 7]
target = 7
assert sol.combinationSum(candidates, target) == [[2, 2, 3], [7]]

candidates = [2, 3, 5]
target = 8
assert sol.combinationSum(candidates, target) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

candidates = [2]
target = 1
assert sol.combinationSum(candidates, target) == []
