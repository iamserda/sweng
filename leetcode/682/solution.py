"""calculate_points solution for leetcode problem 685."""

def calculate_points(operations: list[str]) -> int:
    """Given an array as input, apply the operations, 
    and return the sum of your results. See readme.md for more info. """
    score = []
    for item in operations:
        match item:
            case "C":
                    score.pop()
            case "D":
                    value = score.pop()
                    score.append(value)
                    score.append(value * 2)
            case "+":
                if len(score) >= 2:
                    item1 = score.pop()
                    item2 = score.pop()
                    item3 = item1 + item2
                    score.append(item2)
                    score.append(item1)
                    score.append(item3)
            case item:
                score.append(int(item))
    return sum(score)

assert calculate_points(["5","2","C","D","+"]) == 30
assert calculate_points(["5","-2","4","C","D","9","+","+"]) == 27
assert calculate_points(["1","C"]) == 0
