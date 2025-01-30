# [27. Remove Element](https://leetcode.com/problems/remove-element/description/)

**Difficulty:**Easy

**Topics:** Array, Two Pointers

## Companies

A common question in coding interviews, particularly with companies that focus on efficiency and optimizing algorithms, such as Google, Amazon, and Facebook.

## Hint

Use a two-pointer technique to process elements in one pass. Keep one pointer for iterating through the array and another for the next position to place a non-`val` element.

## Description

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in `nums` which are not equal to `val` to be `k`. To get accepted, you need to do the following:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important, as well as the size of `nums`.
- Return `k`.

### Custom Judge

The judge will test your solution with specific code that checks if your function returns the correct `k` and rearranges `nums` accordingly. If your solution passes these checks, it will be accepted.

### Examples

**Example 1:**

- Input: `nums = [3,2,2,3], val = 3`
- Output: `2, nums = [2,2,_,_]`
- Explanation: Your function should return `k = 2`, with the first two elements of `nums` being 2. It does not matter what you leave beyond the returned `k` (hence they are underscores).

**Example 2:**

- Input: `nums = [0,1,2,2,3,0,4,2], val = 2`
- Output: `5, nums = [0,1,4,0,3,_,_,_]`
- Explanation: Your function should return `k = 5`, with the first five elements of `nums` containing 0, 0, 1, 3, and 4. Note that the five elements can be returned in any order. It does not matter what you leave beyond the returned `k` (hence they are underscores).

### Constraints

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Approach

The efficient way to solve this problem is by using the two-pointer technique. One pointer (`i`) iterates through the array, while another pointer (`k`) tracks the position where the next non-`val` element should be placed. When an element not equal to `val` is found, it is moved to the position indicated by `k`, and `k` is incremented. This method ensures that all elements not equal to `val` are moved to the beginning of the array, and `k` indicates the new length of the array without `val` elements.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/remove-element/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
