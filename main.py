def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    try:
        return quick_sort(less) + [pivot] + quick_sort(greater)
    except RecursionError:
        return arr


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# radix sort using counting sort algorithm
def radix_sort_counting(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        buckets = [[] for _ in range(10)]
        for i in arr:
            buckets[i // exp % 10].append(i)
        arr = [i for bucket in buckets for i in bucket]
        exp *= 10
    return arr
