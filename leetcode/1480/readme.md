# [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/description)

**Difficulty:** Easy

**Topics:** Array, Prefix Sum

## Companies

This problem may appear in technical interviews at companies that are interested in testing candidates' understanding of array manipulation and prefix sums, such as companies working on data processing, analytics, or any software that requires cumulative calculations (e.g., Google, Amazon, Facebook).

## Description

Given an array `nums`. We define a running sum of an array as `runningSum[i] = sum(nums[0]…nums[i])`.

Return the running sum of `nums`.

### Examples

**Example 1:**

```plaintext
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
```

**Example 2:**

```plaintext
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
```

**Example 3:**

```plaintext
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

### Constraints

- `1 <= nums.length <= 1000`
- `-10^6 <= nums[i] <= 10^6`

## Approach

To solve this problem, you can iterate through the array and keep a cumulative sum as you go. For each index, add the current number to the sum of all previous numbers and store it in the result array. This can be done in-place for optimal space usage.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/description)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)