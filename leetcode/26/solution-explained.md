# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

## Intuition

The task of removing duplicates from a sorted array suggests a need for an in-place solution to maintain the array's order while minimizing space usage. My initial thought focuses on the challenge of achieving this without auxiliary data structures. Considering the array is sorted, duplicates would be adjacent, which hints at a two-pointer technique where one pointer tracks the position for the next unique element to be placed, and the other scans through the array.

## Approach

The solution employs a two-pointer technique, where `prev` acts as a slow-runner and `next` as a fast-runner. The `prev` pointer marks the position of the last unique element found, and the `next` pointer iterates through the array. For each distinct element encountered by the `next` pointer (compared to the current element at the `prev` pointer), the element is copied to the position next to `prev`, and `prev` is incremented. This process effectively shifts unique elements towards the front of the array while maintaining their original order, and overwrites duplicates. The length of the unique elements subarray is `prev + 1`, as `prev` is an index.

## Complexity

- Time complexity: $$O(n)$$

  The algorithm iterates through the list a single time, with `next` going from start to finish, making the time complexity linear in the size of the input array.

- Space complexity: $$O(1)$$

  This approach modifies the array in place without using any additional space proportional to the input size, resulting in a constant space complexity.

## Code

```python
def remove_duplicates(nums):
    """Given an array, remove duplicated numbers... see readme for more details."""
    if len(nums) == 0:
        return 0
    prev = 0
    for next in range(1, len(nums)):
        if nums[prev] != nums[next]:
            prev += 1
            nums[prev] = nums[next]
    return prev + 1


# Testing Arenas:
assert remove_duplicates([1, 1, 2]) == 2
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5

```

### Credits, Sources, etc

- [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)