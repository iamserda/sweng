# [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/description/)

**Difficulty:** Medium

**Topics:** String, Two-Pointers

## Description

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space. The input string may also contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces. You need to reduce multiple spaces between two words to a single space in the reversed string.

### Note

- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.

### Examples

**Example 1:**

```plaintext
Input: s = "the sky is blue"
Output: "blue is sky the"
```

**Example 2:**

```plaintext
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

**Example 3:**

```plaintext
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

### Constraints

- `1 <= s.length <= 10^4`
- `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
- There is at least one word in `s`.

## Approach

To solve this problem, consider the following steps:

1. **Trim and Split**: Trim leading and trailing spaces, and then split the string by spaces into words. Note that splitting by spaces should treat multiple spaces as a single delimiter to avoid empty words in the result.

2. **Reverse the Words**: Reverse the order of words obtained from the split operation.

3. **Join the Words**: Join the reversed words with a single space between them to form the final string.

An alternative approach involves two pointers to reverse each word in place and then reverse the entire string to achieve the correct word order without leading or trailing spaces and with only single spaces between words.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)