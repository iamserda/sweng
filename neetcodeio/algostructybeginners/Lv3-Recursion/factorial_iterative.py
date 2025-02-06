def factorial(n):
    if n < 0:
        return
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# TESTING ARENA
assert factorial(5) == 5 * 4 * 3 * 2 * 1
assert factorial(10) == 3628800
assert factorial(0) == 1
assert factorial(1) == 1
assert (
    factorial(100)
    == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
)
