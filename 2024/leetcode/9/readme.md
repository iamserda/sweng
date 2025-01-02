# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

## Difficulty

Easy

## Topics

- Math

## Description

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

### Examples

**Example 1:**

```plaintext
Input: x = 121
Output: true
```

**Example 2:**

```plaintext
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**

```plaintext
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

### Constraints

- `-2^31 <= x <= 2^31 - 1`

## Approach

To solve this problem, you have a few options:

- **Reversing the Number**: You could convert the integer to a string, reverse it, and compare it to the original string. However, this requires extra non-constant space for the string manipulation which might not be allowed.

- **Reversing Half of the Number**: Compare the first half of the number with the reversed second half. If both halves are the same, then the number is a palindrome. This can be done without converting the integer to a string, thus using only constant extra space.

Note that negative numbers are not considered palindromes due to the minus sign. Also, any number that ends with a 0 would not be a palindrome, except for 0 itself, because the leading zero in numbers is not allowed (e.g., the reverse of 10 is 01, which is not the same as 10).

Remember to consider all edge cases, such as negative numbers and numbers with trailing zeros, when implementing your solution.

### Credit, Source, Etc

- Source: [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)