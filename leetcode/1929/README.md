# 1929. [Concatenation of Array Solution](https://leetcode.com/problems/concatenation-of-array/description/)

## Description

This solution is designed to solve the problem titled "1929. Concatenation of Array." The problem is classified as easy and involves creating a new array by concatenating a given integer array with itself.

## Problem Statement

Given an integer array `nums` of length `n`, the goal is to create an array `ans` of length `2n` where `ans[i] == nums[i]` and `ans[i + n] == nums[i]` for `0 <= i < n` (0-indexed). Essentially, `ans` is the concatenation of two `nums` arrays. The task is to return the array `ans`.

### Examples

#### Example 1:

- Input: `nums = [1,2,1]`
- Output: `[1,2,1,1,2,1]`
- Explanation: The array `ans` is formed by concatenating `[nums[0],nums[1],nums[2]]` with itself.

#### Example 2:

- Input: `nums = [1,3,2,1]`
- Output: `[1,3,2,1,1,3,2,1]`
- Explanation: The array `ans` is formed by concatenating `[nums[0],nums[1],nums[2],nums[3]]` with itself.

### Constraints

- `n == nums.length`
- `1 <= n <= 1000`
- `1 <= nums[i] <= 1000`

## Solution Approach

The solution to this problem is straightforward. You simply need to concatenate the original array `nums` with itself. This can be done in various programming languages with different syntaxes but follows the same logic.

### Python Solution

```python
def getConcatenation(nums):
    ans = nums + nums  # Concatenate the list with itself
    return ans
```

### Usage

```python
nums = [1, 2, 1]
print(getConcatenation(nums))
# Output: [1, 2, 1, 1, 2, 1]

nums = [1, 3, 2, 1]
print(getConcatenation(nums))
# Output: [1, 3, 2, 1, 1, 3, 2, 1]
```

## Conclusion

The "Concatenation of Array" problem requires creating a new array that is a concatenation of the given array with itself. The solution involves simple array operations and can be implemented easily in any programming language.

## Credits, Sources, Etc

- Source: [LeetCode](https://leetcode.com/problems/concatenation-of-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)