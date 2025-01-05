def isAnagram(s, t):
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


assert isAnagram("anagram", "gramana") is True
assert isAnagram("rat", "car") is False
assert isAnagram("aa", "a") is False
# print(isAnagram("anagram", "gramana"))
# print(isAnagram("rat", "car"))
# print(isAnagram("aa", "a"))
