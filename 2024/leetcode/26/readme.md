# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

**Difficulty:** Easy

**Topics:** Array, Two Pointers

## Companies

A common interview question for companies focusing on algorithms and data structures, such as Google, Facebook, Amazon, and Microsoft.

## Description

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`. To get accepted, you need to do the following:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially.
- The remaining elements of `nums` are not important, as well as the size of `nums`.
- Return `k`.

### Custom Judge

The judge will test your solution with specific code that checks if your function returns the correct `k` and rearranges `nums` accordingly. If your solution passes these checks, it will be accepted.

### Examples

**Example 1:**

- Input: `nums = [1,1,2]`
- Output: `2, nums = [1,2,_]`
- Explanation: Your function should return `k = 2`, with the first two elements of `nums` being 1 and 2 respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

**Example 2:**

- Input: `nums = [0,0,1,1,1,2,2,3,3,4]`
- Output: `5, nums = [0,1,2,3,4,_,_,_,_,_]`
- Explanation: Your function should return `k = 5`, with the first five elements of `nums` being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned `k` (hence they are underscores).

### Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in non-decreasing order.

## Hint

Use a two-pointer technique to process elements in one pass. Keep one pointer for iterating through the array and another for the next unique element's position.

## Approach

The efficient way to solve this problem is by using the two-pointer technique. One pointer tracks the current position for the next unique element, while the other iterates through the array. Compare each element with the next one and only copy unique elements to the position tracked by the first pointer. This in-place algorithm ensures that the array's unique elements are kept in the same relative order with O(1) extra space.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
