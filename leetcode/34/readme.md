# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Companies

This problem is a popular one among tech companies, including but not limited to Google, Amazon, and Facebook during technical interviews.

## Description

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value. If the `target` is not found in the array, return `[-1, -1]`.

Your algorithm's runtime complexity must be in the order of O(log n), making a straightforward linear scan insufficient due to the time complexity requirements.

### Examples

**Example 1:**

- Input: `nums = [5,7,7,8,8,10], target = 8`
- Output: `[3,4]`

**Example 2:**

- Input: `nums = [5,7,7,8,8,10], target = 6`
- Output: `[-1,-1]`

**Example 3:**

- Input: `nums = [], target = 0`
- Output: `[-1,-1]`

### Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

**Difficulty:** Medium

**Topics:** Array, Binary Search

## Optimized Solution

To achieve the O(log n) time complexity, consider using a binary search algorithm to find the leftmost (first) occurrence of the target value and then again to find the rightmost (last) occurrence. This ensures that even in the worst-case scenario, where the target value occupies a significant portion of the array, the algorithm remains efficient.

## Credits, Sources, Etc

- Source: [LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)