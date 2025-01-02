import random


def digit_in_number(num: int) -> None:
    """Prints each digit within the given integer 'num' arg."""
    if isinstance(num, int):
        result = []
        print(f"Number: {num}")
        while num > 0:
            result.append(num % 10)
            num = int(num / 10)
        result.reverse()
        return result
    # RAINY DAY
    err_object = TypeError(
        f"Error: Expected argument of type 'int'. Received type: {type(num)}")
    print(err_object)
    return []


if __name__ == "__main__":
    print(*digit_in_number("10000"))
    print(*digit_in_number(random.randrange(10**6, 10**7-1)))
    print(digit_in_number((1, 2, 3, 4, 5)))
