"""Given an integer, return the sum of the prime digits in the given integer."""


def sum_of_prime_digits(num):
    """Given an integer, return the sum of the prime digits in the given integer."""
    primes = [2, 3, 5, 7]
    result = 0
    while num > 0:
        n = num % 10
        if int(n) in primes:
            result += n
        num //= 10
    print(result)
    return result or -1


# Tests Arena
assert sum_of_prime_digits(12345) == 10  # True
assert sum_of_prime_digits(123456789) == 17  # True
assert sum_of_prime_digits(4680) == -1  # True
