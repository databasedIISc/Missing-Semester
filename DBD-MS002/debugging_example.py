def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 2):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(bubble_sort([4, 6, 1, 8, 7, 2]))
