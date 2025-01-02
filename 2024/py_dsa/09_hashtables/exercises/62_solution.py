def has_unique_chars(s):
    return len(set(s)) == len(s)

assert has_unique_chars('abcdefg') is True # should return True
assert has_unique_chars('hello') is not True # should return False
assert has_unique_chars('') is True # should return True
assert has_unique_chars('0123456789') is True # should return True
assert has_unique_chars('abacadaeaf') is not True # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""