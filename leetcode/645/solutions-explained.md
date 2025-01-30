# [645. Set Mismatch](https://leetcode.com/problems/set-mismatch/solutions/4695570/645-set-mismatch/)

## Intuition

The problem requires finding two integers in an array: one that appears twice (the duplicate) and one that is missing from the sequence of 1 to n, where n is the length of the array. My first thought is to leverage Python's set operations for efficient search and identification of these numbers, given that sets in Python provide O(1) time complexity for add, remove, and check operations on average.

## Approach

1. **Sort the Input Array**: Although sorting incurs an additional time complexity, it simplifies the identification of the duplicate number through linear traversal.
2. **Identify the Duplicate**: By iterating over the sorted array, compare each element with the next one. If two consecutive elements are identical, we've found our duplicate.
3. **Find the Missing Number**: Utilize set operations. Create a set of all numbers that should appear in the array (from 1 to n) and subtract the set of numbers present in the array. The result is the missing number.
   - This approach avoids additional loops and leverages the efficiency of set operations in Python.

## Complexity

- Time complexity: $$O(n \log n)$$
   - The dominant factor here is the sorting of the array, which is $$O(n \log n)$$. The subsequent operations (finding the duplicate and the missing number) are linear, $$O(n)$$, but they do not change the overall complexity.
- Space complexity: $$O(n)$$
   - The space complexity is primarily due to the creation of sets which store up to `n` integers. Despite modifying the input array in place, the auxiliary space for the sets determines the overall space complexity.

## Code

```python
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return nums
        nums.sort()
        # finding duplicates:
        for i, v in enumerate(nums):
            if i + 1 == len(nums):
                return []
            if v == nums[i + 1]:
                dup_found = v
                break
        set1 = set(i for i in range(1, len(nums) + 1))
        set2 = set(nums)
        item = list(set1.difference(set2))[0]
        return [dup_found, item]
```

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)