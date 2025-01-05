# [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/description/)

## Intuition

Initially, the problem seems straightforward—a simple task of duplicating an array and appending it to the end of itself. This duplication process hints at a direct approach where we iterate through the given array and systematically build the resulting array by appending each element twice, once in its original position and once in the mirrored position in the second half of the result array.

## Approach

The solution involves iterating over a loop that runs twice the length of the input array. During the first half of this loop, we append elements in their original order. When the loop reaches the second half (beyond the length of the original array), we start appending elements from the beginning again. This effectively duplicates the array, appending it to itself. To achieve this, we use a single loop and a conditional statement to decide whether to append the current element or its mirrored element from the first half.

## Complexity

- Time complexity: **O(n)**
  - The algorithm iterates over each element exactly twice, making the time complexity linear in terms of the number of elements in the input array.
- Space complexity: $$O(n)$$
  - We create a new array that is twice the size of the input array, leading to a space complexity that is linearly proportional to the input size.

## Code

```python
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        nums_size = len(nums)
        ans_capacity = 2 * nums_size
        for i in range(ans_capacity):
            if i >= nums_size:
                ans.append(nums[i-nums_size])
                continue
            ans.append(nums[i])
        return ans
```

## Credits, Sources, Etc

- Source: [LeetCode](https://leetcode.com/problems/concatenation-of-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
