class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = list()
        candidates.sort()

        def dfs_with_backtracking(start_index=0, valid_candidates=None, remaining=None):
            if valid_candidates is None:
                valid_candidates = []
            if remaining == 0:
                results.append(list(valid_candidates))
                return
            for index in range(start_index, len(candidates)):
                # Early stopping: since candidates are sorted, no need to check further
                if candidates[index] > remaining:
                    break
                valid_candidates.append(candidates[index])
                dfs_with_backtracking(
                    index, valid_candidates, remaining - candidates[index]
                )
                valid_candidates.pop()

        dfs_with_backtracking(start_index=0, valid_candidates=[], remaining=target)
        return results


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
