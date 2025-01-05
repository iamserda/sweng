# [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Intuition

To find the first and last positions of a target value in a sorted array, my initial thought is to use binary search due to its efficiency in sorted arrays. The goal is to find the extreme positions of the target value, which suggests a need for a modified binary search that can pinpoint the first and last occurrences rather than stopping at the first discovery.

## Approach

The provided solution cleverly employs a binary search algorithm twice. The first binary search is aimed at finding the first occurrence of the target. It does this by adjusting the `right` boundary whenever the target is found, effectively narrowing the search space to the left side of the found target. This process continues until the first occurrence is isolated.

The second binary search is to find the last occurrence of the target. This time, the approach adjusts the `left` boundary when the target is found, shifting focus to the right portion of the found target to isolate the last occurrence. This dual binary search strategy ensures that both the first and last positions of the target are accurately identified.

## Complexity

- Time complexity: $$O(\log n)$$

  Both operations (finding the first and last positions) utilize binary search, which has a time complexity of $$O(\log n)$$ in a sorted array. Since the algorithm performs two binary searches, it maintains the $$O(\log n)$$ complexity, as the constants are dropped in Big O notation.

- Space complexity: $$O(1)$$

  The algorithm uses a fixed amount of space (variables for `left`, `right`, `mid`, `first`, and `last`), which does not scale with the input size, thereby ensuring a constant space complexity.

## Code

```python
class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        left = 0
        right = len(nums) - 1
        first = -1
        last = -1
        
        # Find the first occurrence
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # Reset and find the last occurrence
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return [first, last]
```

## Credits, Sources, Etc

- Source: [LeetCode](https://leetcode.com/problems/concatenation-of-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
