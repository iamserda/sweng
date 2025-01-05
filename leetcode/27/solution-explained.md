# [27. Remove Element Solution](https://leetcode.com/problems/remove-element/solutions/4763137/lc27-beginner-friendly-solution-with-o-n-time-and-o-1-space-by-iamserda)

## Intuition

This problem requires removing all instances of a specific value from an array. The initial thought process involves finding a way to iterate over the array and efficiently remove elements matching the value without disrupting the iteration process.

## Approach

The solution employs a two-pointer technique to solve the problem in-place. The idea is to use two pointers, `left_index` (left) and `right_index` (right), where `left_index` is used to scan through the array from the start, and `right_index` is used to find elements from the end that can replace the elements equal to `val` found by `left_index`. This way, elements are swapped when necessary, and the array is effectively shortened from the right side each time a matching element is found. This process continues until `left_index` and `right_index` meet.

### Steps:

1. Check if the array is empty; if so, return its length.
2. Initialize two pointers, `left_index` at the start of the array and `right_index` at the end.
3. While `left_index` is less than or equal to `right_index`:
    - If the element at `left_index` is the target value `val`, check if it's different from the element at `right_index`.
        - If yes, swap the elements at `left_index` and `right_index`, decrement `right_index`, remove the last element (now a duplicate after swap), and increment `left_index`.
        - If no, just decrement `right_index` and remove the last element, as it's a match.
    - If the element at `left_index` is not `val`, increment `left_index`.
4. Return the new length of the array.

## Complexity

- **Time complexity:** $$O(n)$$ - The solution iterates over the array once with two pointers moving towards each other, making it linear in the size of the input array.
- **Space complexity:** $$O(1)$$ - The operation is performed in-place, using a constant amount of extra space.

## Code

```python
def remove_element(nums: list[int], val: int) -> int:
    """Given an integer array nums and an integer val, remove all occurrences of val in nums **in-place**. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val."""
    if not nums:
        return 0

    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        if nums[left_index] == val:
            if nums[left_index] == nums[right_index]:
                right_index -= 1
            else:
                nums[left_index], nums[right_index] = nums[right_index], nums[left_index]
                left_index += 1
                right_index -= 1
            nums.pop()
            continue
        left_index += 1
    return len(nums)


arr = [3, 2, 2, 3]
assert remove_element(arr, 3) == 2
arr = [0, 1, 2, 2, 3, 0, 4, 2]
assert remove_element(arr, 2) == 5
arr = [1]
assert remove_element(arr, 1) == 0
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert remove_element(arr, 1) == 0
```

### Credit, Source, Etc

- Source: [Solution](https://leetcode.com/problems/remove-element/solutions/4763137/lc27-beginner-friendly-solution-with-o-n-time-and-o-1-space-by-iamserda) on LeetCode.
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)