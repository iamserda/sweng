# 287: Solution with step-by-step explanation by Marlen09

## Intuition

**Approach**:
The problem can be treated as a linked list cycle detection problem.
Since there is only one duplicate number, the array can be treated as a linked list,where each number points to the index indicated by the value. For example, if nums[0] = 2, it means that there is a pointer from index 0 to index 2. We can use Floyd's Tortoise and Hare algorithm to detect the cycle in the linked list, which is guaranteed to exist since there is at least one duplicate number in the list. Once we have detected the cycle, we can reset the tortoise to the start of the list, and move both the tortoise and hare at the same speed until they meet again. The point where they meet will be the duplicate number.

# Efficiency or Complexity

- Time complexity: `O(n) 83.46%`
- Space complexity: `O(1) 88.35%`

```python
class Solution:
  def findDuplicate(self, nums: List[int]) -> int:
    # Using Floyd's Tortoise and Hare algorithm
    # to detect the cycle in the linked list
    tortoise = nums[0]
    hare = nums[0]
    
    # Move tortoise and hare until they meet
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    # Reset tortoise to the start of the list
    tortoise = nums[0]
    
    # Move tortoise and hare at the same speed until they meet again
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    
    # Return the duplicate number
    return tortoise
```

Solution by [Marlen09](https://leetcode.com/Marlen09/)
