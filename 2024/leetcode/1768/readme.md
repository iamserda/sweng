# [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/)

## Difficulty

Easy

## Topics

- String
- Two Pointers

## Companies

This problem may be of interest in interviews with companies that focus on string manipulation and algorithms, including tech giants and startups.

## Description

Given two strings `word1` and `word2`, merge them in an alternating fashion starting with `word1`. If a string is longer than the other, append the additional characters onto the end of the merged string.

To elaborate, the resulting string should be the first letter of `word1`, then the first letter of `word2`, followed by the second letter of `word1`, then the second letter of `word2`, and so on. If the letters in `word1` are exhausted, the remaining letters of `word2` continue in the merged string and vice versa.

### Examples

**Example 1:**

- Input: `word1 = "abc", word2 = "pqr"`
- Output: `"apbqcr"`
- Explanation: The characters of `word1` and `word2` are merged alternately: `a` from `word1`, then `p` from `word2`, `b` from `word1`, `q` from `word2`, and so on. Since both strings have the same length, the merging stops once all characters are used.

**Example 2:**

- Input: `word1 = "ab", word2 = "pqrs"`
- Output: `"apbqrs"`
- Explanation: After merging `ab` and `pq` alternately, `rs` from `word2` is appended to the end as `word1` is shorter.

**Example 3:**

- Input: `word1 = "abcd", word2 = "pq"`
- Output: `"apbqcd"`
- Explanation: After merging `ab` and `pq` alternately, `cd` from `word1` is appended to the end as `word2` is shorter.

### Constraints

- `1 <= word1.length, word2.length <= 100`
- `word1` and `word2` consist of lowercase English letters.

## Approach

The problem can be solved by iterating through the characters of both strings simultaneously using two pointers. During each iteration, append the current character from `word1` to the result, followed by the current character from `word2`. If one string is exhausted before the other, append the remaining characters of the longer string to the result. This can be achieved efficiently using a loop and conditionals to check the end of each string.

This approach ensures that the characters are merged alternately and handles cases where the strings are of unequal lengths.

### Credit, Source, Etc

- Source: [LeetCode](https://leetcode.com/problems/merge-strings-alternately/description/)
- [github:  @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin:    @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
