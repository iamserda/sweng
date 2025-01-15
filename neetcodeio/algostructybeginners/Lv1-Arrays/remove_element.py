def remove_element(arr: list, elem: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        if elem == arr[left]:
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
            continue
        left += 1
    return left

assert remove_element([0, 2, 1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2], 2) == 7
