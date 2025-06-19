def is_palindrome(my_str: str):
    """Given a string as argument, returns true if the string forward, and backward the same, is a palindrome. Otherwise, returns false."""
    if len(my_str):
        start_index = 0
        end_index = len(my_str) - 1
        # using two-pointers method
        while start_index <= end_index:
            if my_str[start_index] == my_str[end_index]:
                start_index += 1
                end_index -= 1
            else:
                return False
        return True
    return False


pal1 = "abcba"  # true
pal2 = "abcde"

print(is_palindrome(pal1))  # True"
print(is_palindrome(pal2))  # False
