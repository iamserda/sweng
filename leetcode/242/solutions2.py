def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # Early return if lengths differ
    if len(s) != len(t):
        return False

    char_count = {}

    # Increment for s, decrement for t
    for i, v in enumerate(s):
        char_count[v] = char_count.get(s[i], 0) + 1
        char_count[t[i]] = char_count.get(t[i], 0) - 1

    # Check all counts have returned to zero
    for count in char_count.values():
        if count != 0:
            return False

    return True


assert isAnagram("anagram", "gramana") is True
assert isAnagram("rat", "car") is False
assert isAnagram("aa", "a") is False
