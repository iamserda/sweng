def isPalindrome(x: int) -> bool:
    # conversion to string, 
    # compare reversed string to original string.
    return str(x) == str(x)[::-1]
