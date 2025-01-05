# LC217 - Solution Explained

## Intuition

To identify duplicates in a collection efficiently, a set is an ideal data structure due to its inherent property of disallowing duplicate elements. While a dictionary could track the frequency of each element, it's unnecessarily complex for merely detecting the presence of duplicates. In this context, a set's simplicity and efficiency make it the optimal choice.

## Approach

To solve this problem, the approach is straightforward and involves the following steps:

1. Initialize an empty set to track observed elements.
2. Iterate through each element in the input list.
3. For each element, perform a constant-time check to determine if it's already in the set (indicating a duplicate).
   - If a duplicate is found, return True immediately, as we've met our condition for identifying duplicates.
   - If the element is not in the set, add it to the set and continue to the next element.
4. Continue this process until all elements have been checked.
5. If the iteration completes without finding any duplicates, return False, indicating all elements are unique.

Alternatively, a more concise method involves leveraging the size comparison between the input list and its set representation:

- Convert the list into a set, which removes any duplicates.
- Compare the length of the original list to the length of the set.
  - If the set's length is less than the list's, it indicates the presence of duplicates.
  - This method succinctly determines the existence of duplicates through a simple length comparison.

## Complexity Analysis

- Time Complexity: O(n). The algorithm iterates through each element of the list exactly once. Membership checks and additions to the set are performed in constant time, O(1), thanks to hashing.
- Space Complexity: O(n). In the worst-case scenario, where all elements are unique, the set grows to the same size as the input list, necessitating O(n) space.

## Code

```python
class Solution1:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False

class Solution2:
    def containsDuplicateWay2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return False if len(set(nums)) == len(nums) else True

class Solution3:
    def containsDuplicateWay2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return None
        nums.sort()
        i = 0  # indexer
        size = len(nums)
        while i < (size - 1):
            if nums[i] == nums[i + 1]:
                return True
            i += 1
        return False
```

[tw: @iamserda](https://twitter.com/iamserda)
[in: @iamserda](https://linkedin.com/in/iamserda)
[gh: @iamserda](https://github.com/iamserda)