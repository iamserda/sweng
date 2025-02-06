def factorial(num):
    # base case, stops the recursion.
    if num <= 1:
        return 1
    else:
        # recursive case
        return num * factorial(num - 1)


# n! = n * (n-1)!
# 1! = 1
# 0! = 1
# Space complexity is O(n) because we are stacking
# each recursive call pending until we find a base case
# where num is 1 or num is 0.

# A never ending recursion leads to memory stack,
# area of memory where function data are stored
# temporarily while the function is running.
# Too many of these recursive-calls will eventually lead to
# a stack overflow, too much data on

assert factorial(5) == 5 * 4 * 3 * 2 * 1
assert factorial(10) == 3628800
assert factorial(0) == 1
assert factorial(1) == 1
assert (
    factorial(100)
    == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
)

ans = str(factorial(10))
print(ans, len(ans))
