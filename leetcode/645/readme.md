# [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/solutions/4695570/645-set-mismatch/)

## Description

This challenge involves a set of integers `s`, which initially contains all numbers from 1 to `n`. However, due to an error, one of the numbers in `s` got duplicated to another number in the set, leading to the repetition of one number and the loss of another.

You are provided with an integer array `nums` that represents the data status of this set after the error. Your task is to find the number that occurs twice and the number that is missing and return them in the form of an array.

## Examples

### Example 1:

- **Input:** `nums = [1,2,2,4]`
- **Output:** `[2,3]`

### Example 2:

- **Input:** `nums = [1,1]`
- **Output:** `[1,2]`

## Constraints

- `2 <= nums.length <= 104`
- `1 <= nums[i] <= 104`

## Topics

- Array
- Hash Table
- Math
- Bit Manipulation
- Sorting

## Companies

- This challenge is commonly asked in technical interviews at various companies.

## Solution Approach

1. Iterate through the given array to track the frequency of each number.
2. Identify the number that appears twice and the number that is missing by comparing with the expected frequency.
3. Return the duplicated number and the missing number as an array.

## Tips

- Consider using a hash map to keep track of the frequencies of each element in the array.
- Alternatively, solve it with constant space by using mathematical formulas or bit manipulation techniques.

## Difficulty

- Easy

## Credits, Source, Etc

- Source: [LeetCode Problem 645](https://leetcode.com/problems/set-mismatch/solutions/4695570/645-set-mismatch/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)