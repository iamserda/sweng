
# Palindrome Checker for Alphanumeric Strings

## Intuition
The task is to determine if a given string is a palindrome, considering only alphanumeric characters and ignoring cases. This problem requires filtering out non-alphanumeric characters and achieving case insensitivity, aligning with common definitions of palindromes in programming contexts.

## Approach
The solution employs a two-pointer technique to compare characters from the beginning and end of the string, moving towards the center. It involves several key steps:
- **Initialization**: Two pointers, `left_index` and `right_index`, are initialized to point to the start and end of the string, respectively.
- **Traversal**: The algorithm iterates, moving the pointers towards each other until they meet or cross, performing the following checks at each step:
  - **Alphanumeric Check**: If the character at either pointer is not alphanumeric, the pointer is moved inward (left pointer moves right, right pointer moves left) without making any comparison.
  - **Case Insensitive Comparison**: If both characters are alphanumeric, they are compared in a case-insensitive manner. If they do not match, the function returns `False`, indicating the string is not a palindrome.
  - **Pointer Adjustment**: If the characters match, both pointers are moved towards the center, and the comparison continues.
- **Conclusion**: If all comparisons are successful (indicating a match for all mirrored characters), the function returns `True`, confirming the string is a palindrome.

## Complexity
- **Time Complexity**: $$O(n)$$ - The algorithm iterates over each character at most twice (once for each pointer), where `n` is the length of the string. The operations performed at each step (checking if a character is alphanumeric, converting to lowercase, and comparing characters) are all constant time, leading to a linear time complexity.
- **Space Complexity**: $$O(1)$$ - The space used by the algorithm does not scale with the input size. The additional memory used (for pointers and temporary variables) is constant, regardless of the string's length.

## Code
```python
def isPalindrome(s: str) -> bool:
    left_index = 0
    right_index = len(s) - 1

    while left_index <= right_index:
        if not s[left_index].isalnum():
            left_index += 1
            continue
        if not s[right_index].isalnum():
            right_index -= 1
            continue
        if s[right_index].lower() != s[left_index].lower():
            return False
        left_index += 1
        right_index -= 1
    return True

# Test cases
assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
```

### Credit, Source, Etc

- This solution is a practical application of string manipulation and validation techniques, focusing on efficiently identifying palindromic patterns in strings with mixed character types.

- Crafted with the intent to demonstrate clear and effective use of Python's string handling capabilities, the solution is a straightforward yet robust approach to a common algorithmic challenge.

Designed to be both educational and practical, this palindrome checker showcases fundamental programming concepts, including iteration, conditionals, and string operations, in solving real-world problems.

- Source: [LeetCode](https://leetcode.com/problems/merge-sorted-array/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)