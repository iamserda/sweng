# [Two Sum](https://leetcode.com/problems/two-sum/)

## Intuition
When first approaching the "Two Sum" problem, it's clear that the challenge lies in efficiently finding two numbers in an array that add up to a specific target. The straightforward solution of checking every pair is too slow, so there's a need for a method that can find the solution in a single pass through the array.

## Approach
The solution utilizes a hash table to store the indices of the numbers as they're iterated over. For each number, it calculates its complement by subtracting the number from the target. It then checks if this complement is already in the hash table:
- If it is, it means a previously visited number is the required pair to reach the target, and the function returns the indices of these two numbers.
- If not, the current number's value and its index are stored in the hash table for potential future matches.

This method allows us to find the two numbers in a single pass through the array, significantly speeding up the process.

## Complexity
- Time complexity: $$O(n)$$

  The algorithm passes through the list only once. Hash table insertion and lookup have an average time complexity of $$O(1)$$, so the overall time complexity is linear with respect to the array's length.

- Space complexity: $$O(n)$$

  In the worst case, the extra space required depends on the number of items stored in the hash table, which stores up to `n - 1` elements where `n` is the number of elements in the input array.

## Code
```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in complements:
                return [complements[complement], index]
            complements[value] = index
```

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/two-sum/)
- [GitHub: @iamserda](https://github.com/iamserda)
- [Twitter: @iamserda](https://twitter.com/iamserda)
- [LinkedIn: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in NYC by [@iamserda](https://www.twitter.com/iamserda)