# Anagram Solution

# Intuition
To determine if two strings are anagrams of each other, the approach is to count the occurrences of each character in both strings and then compare these counts. If the counts for all characters are the same in both strings, then they are anagrams of each other. An anagram, by definition, is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.

# Approach
The algorithm implemented involves creating two dictionaries (hash maps) to store the counts of each character in each of the two input strings. Here's a step-by-step breakdown:
1. **Check for Empty Strings**: If either of the input strings is empty, return `False` as they cannot be anagrams.
2. **Create and Populate Character Count Dictionaries**: Iterate through each character in both strings. For each string, if a character is encountered that is already in its respective dictionary, increment the count. If it's not present, add it to the dictionary with a count of 1.
3. **Compare Dictionary Sizes**: If the sizes of the two dictionaries are different, the strings cannot be anagrams and return `False`.
4. **Compare Dictionary Entries**: Check each entry (character and count) in the first string's dictionary against the second string's dictionary. If any character-count pair does not match exactly, return `False`.
5. **Anagrams**: If all checks pass, the strings are anagrams, and return `True`.

# Complexity
- Time complexity: $$O(n + m)$$ where $$n$$ is the length of string `s` and $$m$$ is the length of string `t`. This is because each string is iterated over once to populate the dictionaries and then the dictionaries are compared.
- Space complexity: $$O(n + m)$$ where $$n$$ is the distinct characters in string `s` and $$m$$ is the distinct characters in string `t`. In the worst case, all characters are unique, leading to dictionaries whose sizes are proportional to the lengths of the strings.

# Code
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
