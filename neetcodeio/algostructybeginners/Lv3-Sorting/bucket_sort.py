def bucket_sort(arr: list):
    set_a = set(arr)
    bucket = [0] * len(set_a)
    for item in arr:
        bucket[item] += 1

    sorted_arr = []
    for index in range(len(bucket)):
        for j in range(bucket[index]):
            sorted_arr.append(index)

    return sorted_arr


assert bucket_sort([2, 1, 2, 0, 0, 2]) == [0, 0, 1, 2, 2, 2]
