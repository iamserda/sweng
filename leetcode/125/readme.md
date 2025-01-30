
# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

**Difficulty:** Easy

**Topics:** String, Two-Pointers

## Companies

This type of question is commonly asked in interviews at tech companies such as Google, Amazon, Facebook, and Microsoft to assess a candidate's understanding of strings and their manipulation.

## Description

A phrase is considered a palindrome if, after converting all uppercase letters to lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, determine if it is a palindrome, returning `true` if it is, or `false` otherwise.

### Examples

**Example 1:**

- Input: `s = "A man, a plan, a canal: Panama"`
- Output: `true`
- Explanation: After converting to lowercase and removing non-alphanumeric characters, `"amanaplanacanalpanama"` is a palindrome.

**Example 2:**

- Input: `s = "race a car"`
- Output: `false`
- Explanation: `"raceacar"` is not a palindrome.

**Example 3:**

- Input: `s = " "`
- Output: `true`
- Explanation: `s` is an empty string `""` after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.

### Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Approach

To verify if `s` is a palindrome under the given conditions, you can use a two-pointer technique:

1. Normalize the string `s` by converting it to lowercase and removing non-alphanumeric characters. This can be done using a simple loop and checking each character's ASCII values or using built-in functions in higher-level languages.
2. Initialize two pointers, one at the beginning of the string (`left`) and one at the end (`right`).
3. Move `left` forward and `right` backward, comparing characters at these positions at each step.
   - If at any point the characters do not match, return `false`.
   - Continue this process while `left < right`.
4. If the entire string is traversed without mismatches, return `true`.

This approach efficiently checks for palindromicity by considering only alphanumeric characters and ignoring cases, adhering to the problem's constraints.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/valid-palindrome/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)