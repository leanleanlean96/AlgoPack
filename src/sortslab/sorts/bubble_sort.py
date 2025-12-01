def bubble_sort(arr: list[int]) -> list[int]:
    length: int = len(arr)
    for i in range(length):
        swapped: bool = False
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr