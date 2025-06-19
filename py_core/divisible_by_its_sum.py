def divisible_by_its_sum(my_int: int) -> int:
    """Given some integer, return sum of numbers if my int divided
    by sum of its constituants, else return -1"""
    a = my_int // 10
    b = my_int % 10
    sum_of_const = a + b
    if my_int % sum_of_const == 0:
        return sum_of_const
    return -1


print(divisible_by_its_sum(23))  # -1
print(divisible_by_its_sum(81))  # 9
