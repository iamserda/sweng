
def isValid(a_string: str) -> bool:
    """
    Given a string, return True if the parentheses, brackets 
    and curly-braces are in valid order.
    """
    closers = {
        ")": "(",
        "]":"[" ,
        "}":"{"
    }
    
    my_stack = []
    
    for item in a_string:
        last_index = len(my_stack) - 1
        if item in closers:
            if not my_stack:
                return False
            elif my_stack[last_index] == closers[item]:
                my_stack.pop()
            else:
                return False
        else:
            my_stack.append(item)
    
    return True if len(my_stack) == 0 else  False

# TESTING ARENA:
assert isValid("()[]{}") == True
assert isValid("{()[]}") == True
assert isValid("([]{})") == True
assert isValid(")[]{}") == False