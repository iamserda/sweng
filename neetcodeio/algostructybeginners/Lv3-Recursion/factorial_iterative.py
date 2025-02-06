def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


assert factorial(5) == 5 * 4 * 3 * 2 * 1
