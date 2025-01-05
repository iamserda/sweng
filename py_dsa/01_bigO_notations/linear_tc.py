## WRITE THE PRINT_ITEMS FUNCTION HERE ##
def linear_time(n):
    """showing an example of linear-time complexity"""
    for i in n:
        print(f"Number: {i}")


def linear_time_example(arr: list[int]):
    """Calculate the sum of the elements of an array of integers."""
    total = 0
    for num in arr:
        total += num
    return total


arr = [1, 2, 3, 4, 5]
result = linear_time_example(arr)
print(result)  # The time taken increases linearly with the size of the array.

def still_linear_time(n):
    """showing an example of linear-time complexity"""
    for idx in n:
        print(f"Number: {idx}")

    for jdx in n:
        print(f"Number: {jdx * jdx}")


# DO NOT CHANGE THIS LINE:
linear_time(range(10))
still_linear_time(range(10))
