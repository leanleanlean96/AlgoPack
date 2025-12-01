def partition(arr: list[int], low: int, high: int) -> int:
    i: int = low
    pivot: int = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i ]
    return i

def quickSort(arr, low: int = 0, high: int | None = None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition(arr, low, high)
        
        quickSort(arr, pivot_index + 1, high)
        quickSort(arr, low, pivot_index - 1)
    return arr