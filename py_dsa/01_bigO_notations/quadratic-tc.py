def bubble_sort(arr):
    """Bubble-Sort"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [5, 2, 9, 1, 5, 6]
bubble_sort(arr)
# Bubble sort has O(n^2) time complexity for worst and average cases.
print(arr)
