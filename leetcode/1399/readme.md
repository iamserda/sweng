# [1399. Count Largest Group](https://leetcode.com/problems/count-largest-group/description/)

**Difficulty:** Easy

**Topics:** Hash Table, Math

## Description

Given an integer `n`, you need to find the number of groups having the largest size. Each integer from `1` to `n` is grouped according to the sum of its digits.

Return the number of groups with the largest size.

### Examples

**Example 1:**

```plaintext
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of digits:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups having largest size.
```

**Example 2:**

```plaintext
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] with size 1.
```

### Constraints

- `1 <= n <= 10^4`

## Approach

To solve this problem, follow these steps:

1. **Calculate digit sums**: For each integer from `1` to `n`, calculate the sum of its digits.

2. **Grouping**: Use a dictionary to store the counts for each digit sum.

3. **Find largest group size**: Determine the largest size among all groups.

4. **Count largest groups**: Count how many groups have this largest size.

This method leverages hash tables (dictionaries) for efficient grouping and counting.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/count-largest-group/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)