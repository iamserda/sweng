# [39. Combination Sum](https://leetcode.com/problems/combination-sum/description/)

## Intuition
The problem asks for all unique combinations of numbers from a given list (`candidates`) that sum up to a target value. Each number in `candidates` can be used an unlimited number of times. This naturally suggests a backtracking approach, where we explore all possible combinations recursively, pruning paths that exceed the target.

## Approach
The solution uses depth-first search (DFS) with backtracking:
- **Sorting**: The `candidates` list is sorted to allow early stopping when a candidate exceeds the remaining target.
- **Backtracking Function**: The recursive function `dfs_with_backtracking` takes the current index, the current combination (`valid_candidates`), and the remaining sum to reach the target.
    - If the remaining sum is zero, the current combination is a valid solution and is added to the results.
    - For each candidate starting from `start_index`, if it does not exceed the remaining sum, it is added to the current combination, and the function recurses with the updated remaining sum.
    - After recursion, the candidate is removed (backtracked) to explore other possibilities.
- **No Duplicates**: By always passing the current index (not `index + 1`), the same candidate can be reused multiple times.

## Complexity
- **Time complexity**: The time complexity depends on the number of candidates (`n`) and the target value (`t`). In the worst case, the algorithm explores all possible combinations, which can be approximated as $$O(n^{t / \text{min}(c)})$$, where `min(c)` is the smallest candidate value. Sorting and pruning reduce the number of combinations significantly.
- **Space complexity**: $$O(t)$$, due to the recursion stack and the space needed to store the current combination.

## Code
```python
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
            results = list()
            candidates.sort()

            def dfs_with_backtracking(start_index=0, valid_candidates, remaining):
                if remaining == 0:
                        results.append(list(valid_candidates))
                        return
                for index in range(start_index, len(candidates)):
                        # Early stopping: since candidates are sorted, no need to check further
                        if candidates[index] > remaining:
                                break
                        valid_candidates.append(candidates[index])
                        dfs_with_backtracking(index, valid_candidates, remaining - candidates[index])
                        valid_candidates.pop()

            dfs_with_backtracking(start_index=0, valid_candidates=[], remaining=target)
            return results


sol = Solution()
# Test case 1: Target is 7, expecting combinations that sum to 7 using [2, 3, 6, 7]
candidates = [2, 3, 6, 7]
target = 7
assert sol.combinationSum(candidates, target) == [[2, 2, 3], [7]]

# Test case 2: Target is 8, expecting combinations that sum to 8 using [2, 3, 5]
candidates = [2, 3, 5]
target = 8
assert sol.combinationSum(candidates, target) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

# Test case 3: Target is 1, expecting no combinations since 2 is greater than the target
candidates = [2]
target = 1
```

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/sort-colors/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)