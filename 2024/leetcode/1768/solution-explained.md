# [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/)

## Intuition
When presented with two strings, the task of merging them alternately character by character suggests an iterative approach. The intuitive method is to loop through the strings, appending one character from each string to a new string in turn. The challenge lies in handling strings of unequal length, ensuring that the remaining characters from the longer string are correctly appended after exhausting the shorter string.

## Approach
The `Solution` class implements the `mergeAlternately` method, which creates a new string by alternately merging characters from `word1` and `word2`:
- Determine `count`, the length of the longer string, to use as the loop's range.
- Iterate up to `count`, during each iteration:
  - If the current index is within the bounds of both `word1` and `word2`, append the current character from each to `word3`.
  - If the current index is beyond the length of `word1`, only append characters from `word2` to `word3`.
  - If the current index is beyond the length of `word2`, only append characters from `word1` to `word3`.
- This approach ensures that all characters from both strings are included in the final merged string, `word3`, in an alternating fashion, with any remaining characters from the longer string appended at the end.

## Complexity
- **Time Complexity**: $$O(n)$$, where $$n$$ is the length of the longer string between `word1` and `word2`. The loop runs a maximum of `n` times, performing constant-time operations within each iteration.
- **Space Complexity**: $$O(n)$$, where $$n$$ is the combined length of `word1` and `word2`. This accounts for the space required to store the new string `word3`.

## Code
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """Given two strings, return a string that's made
        of the chars from string1 and string where characters alternate
        between string1 and string2. ex: "abc" and "xyz" => "axbycz". """
        count = len(word1) if len(word1) >= len(word2) else len(word2)
        word3 = ""
        for i in range(count):
            if i < len(word2) and i < len(word1):
                word3 += word1[i]
                word3 += word2[i]
                continue
            if i >= len(word1):
                word3 += word2[i]
                continue
            else:
                word3 += word1[i]
        return word3
```

### Credit, Source, Etc
- This solution showcases a straightforward approach to solving problems that involve iterating over and manipulating strings based on their lengths and positions of characters.
- Designed to efficiently merge two strings in an alternate fashion, this method emphasizes simplicity and effectiveness in handling strings of varying lengths.

Crafted to illustrate the principles of string manipulation and conditional logic within iterative constructs, this solution provides a clear example of applying basic programming concepts to achieve a desired outcome in string processing tasks.

- Source: [LeetCode](https://leetcode.com/problems/crawler-log-folder/description)
- [github: @iamserda](https://github.com/iamserda)
- [twitter: @iamserda](https://twitter.com/iamserda)
- [linkedin: @iamserda](https://linkedin.com/in/iamserda)

Made with 🤍🫶🏿 in N🗽C by [@iamserda](https://www.twitter.com/iamserda)
