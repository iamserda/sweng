def isPalindrome(s: str) -> bool:
        left_index = 0
        right_index = len(s)-1
        print(left_index, right_index)

        while left_index <= right_index:
            if not s[left_index].isalnum():
                left_index += 1
                continue
            if not s[right_index].isalnum():
                right_index -= 1
                continue
            print("Left:",s[left_index], left_index)
            print("Right:",s[right_index], right_index)
            if s[right_index].lower() != s[left_index].lower():
                return False
            left_index += 1
            right_index -= 1
        return True
    
assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
