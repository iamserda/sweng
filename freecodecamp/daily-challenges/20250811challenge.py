"""
Credit: FreeCodeCamp.org

Original_Url: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-08-11

Date: 2025-08-11

Challege:
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.
The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character.

Test:
1. is_balanced("racecar") should return True.
2. is_balanced("Lorem Ipsum") should return True.
3. is_balanced("Kitty Ipsum") should return False.
4. is_balanced("string") should return False.
5. is_balanced(" ") should return True.
6. is_balanced("abcdefghijklmnopqrstuvwxyz") should return False.
7. is_balanced("123A#b!E&*456-o.U") should return True.

"""


def is_balanced(s):
    """Start Coding Your Solution Here:"""


assert is_balanced("racecar") is True
assert is_balanced("Lorem Ipsum") is True
assert is_balanced("Kitty Ipsum") is False
assert is_balanced("string") is False
assert is_balanced(" ") is True
assert is_balanced("abcdefghijklmnopqrstuvwxyz") is False
assert is_balanced("123A#b!E&*456-o.U") is True
