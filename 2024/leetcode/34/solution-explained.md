# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Intuition

The task is to find the starting and ending position of a given target value in a sorted array. My first thought is to leverage the sorted nature of the array to find the target efficiently. However, a linear scan could also work but might not be the most efficient method, especially for large arrays.

## Approach

The approach implemented in the provided code is a linear scan through the array. It iterates over each element, comparing it with the target value. When it encounters the target for the first time, it records this position as both the first and last occurrence (initially). For subsequent encounters of the target value, it updates the last occurrence position. This approach guarantees that we find the first and last positions of the target value if it exists in the array.

## Complexity

- Time complexity: $$O(n)$$
  
  The reason for this is that, in the worst case, the algorithm needs to iterate through the entire array to find the first and last occurrences of the target value.

- Space complexity: $$O(1)$$

  The space complexity is constant because the solution uses a fixed amount of space (a few variables) regardless of the input array size.

## Code

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = None
        last = None

        for index, value in enumerate(nums):
            if value == target:
                if first is None:
                    first = index
                    last = index
                    continue
                last = index
        return [-1, -1] if first is None else [first, last]
```

## Credits, Sources, Etc

- Source: [LeetCode](https://leetcode.com/problems/concatenation-of-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
