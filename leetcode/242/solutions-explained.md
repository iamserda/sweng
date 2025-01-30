# Anagram Solution Explained

## Intuition

To determine if two strings, `s` and `t`, are anagrams of each other, the strategy is to count the occurrences of each character in both strings. If both strings have the same characters with the exact same number of occurrences for each character, they are anagrams.

## Approach

1. **Early Exit**: If either `s` or `t` is empty, return `False` immediately since one string cannot be an anagram of the other if one of them is empty.
2. **Character Count**: Use two dictionaries to count the occurrences of each character in `s` and `t` respectively.
    - Iterate through each character in `s`, adding to `s_dict` or incrementing the existing count.
    - Repeat the process for `t` with `t_dict`.
3. **Length Check**: If the number of unique characters in `s` and `t` (the lengths of `s_dict` and `t_dict`) differ, the strings cannot be anagrams, return `False`.
4. **Character and Count Verification**: Iterate through `s_dict`, checking if each character and its count match exactly in `t_dict`. If there's any discrepancy, return `False`.
5. If all checks pass, the strings are anagrams, return `True`.

## Complexity

- Time complexity: $$O(n)$$ - The algorithm iterates over each character in both strings exactly once, where `n` is the length of the longer string. The final check for equality also operates within $$O(n)$$ because dictionary lookups and comparisons are $$O(1)$$ on average.
- Space complexity: $$O(n)$$ - Two dictionaries are used to store character counts for both strings, which in the worst case (all unique characters), require space proportional to the length of the strings.

## Code

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not t or not s:
            return False

        t_dict = {}
        s_dict = {}

        for i in s:
            if i in s_dict:
                s_dict[i] += 1
                continue
            s_dict[i] = 1

        for i in t:
            if i in t_dict:
                t_dict[i] += 1
                continue
            t_dict[i] = 1
        if len(s_dict) != len(t_dict):
            return False

        for k, v in s_dict.items():
            if (k, v) not in t_dict.items():
                return False

        return True
```

gh: [@iamserda](https://github.com/iamserda)

tw: [@iamserda](https://twitter.com/iamserda)

in: [@iamserda](https://linkedin.com/in/iamserda)

Builts with 🤍🫶🏿 in N🗽C by[@iamserda](https://www.twitter.com/iamserda)
