## WRITE THE PRINT_ITEMS FUNCTION HERE ##
def quadratic_time(search_list, search_item):
    """showing an example of quadratic-time complexity"""
    start = 0
    end = len(search_list) - 1
    while start <= end:
        mid = (end + start) // 2
        if search_list[mid] == search_item:
            return mid
        if search_item > search_list[mid]:
            start = mid + 1
            continue
        end = mid - 1
    return -1


# TESTS ARENA;
# DO NOT CHANGE ANY LINES BELOW:
S = 80
n = list(range(0, 101, 5))
index = quadratic_time(n, S)
print(f"Found at index: {index}" if index != -
      1 else f"{S} is NOT found in the list.")

S = 180
index = quadratic_time(n, S)
print(f"Found at {index}" if index != -1 else f"{S} is NOT found in the list.")

S = -19
index = quadratic_time(n, S)
print(f"Found at {index}" if index != -1 else f"{S} is NOT found in the list.")
