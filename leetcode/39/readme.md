# [39. Combination Sum](https://leetcode.com/problems/combination-sum/description/)

**Difficulty:** Medium

**Topics:** Array, Backtracking

## Description

Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.

The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

### Note

- All numbers (including `target`) will be positive integers.
- The solution set must not contain duplicate combinations.

### Examples

**Example 1:**

```plaintext
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation: 2 and 3 can be used multiple times.
```

**Example 2:**

```plaintext
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3:**

```plaintext
Input: candidates = [2], target = 1
Output: []
```

### Constraints

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are distinct.
- `1 <= target <= 40`

## Approach

To solve this problem, consider the following steps:

1. **Backtracking**: Use a backtracking approach to explore all possible combinations. At each step, decide whether to include the current candidate and recursively try to reach the target.
2. **No Duplicates**: Since each number can be used unlimited times, do not increment the index when including the current candidate.
3. **Pruning**: If the current sum exceeds the target, backtrack immediately.

A typical implementation sorts the candidates (optional for this problem), then recursively builds combinations, adding them to the result when the sum matches the target.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/combination-sum/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
