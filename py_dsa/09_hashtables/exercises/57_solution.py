def first_non_repeating_char(s:str) -> int:
    dictio = {}
    for char in s:
        if dictio.get(char) is None:
            dictio[char] = 1
        else:
            dictio[char] += 1

    for i, char in enumerate(s):
        if dictio[char] == 1:
                return char

assert first_non_repeating_char('leetcode') == "l"
assert first_non_repeating_char('hello') == "h"
assert first_non_repeating_char('aabbcc') is None
