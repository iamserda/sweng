def isValid(string: str) -> bool:
    openers = set(list("{[("))
    matching_set = {"{}", "[]", "()"}
    stack = []

    for char in string:
        if char in openers:
            stack.append(char)
            continue
        if not stack:
            return False
        if stack[-1] + char in matching_set:
            stack.pop()
            continue
        return False

    if len(stack) == 0:
        return True
    return False


assert isValid("[") == False
assert isValid("()") == True
assert isValid("()[]{}") == True
assert isValid("(]") == False
assert isValid("([])") == True
