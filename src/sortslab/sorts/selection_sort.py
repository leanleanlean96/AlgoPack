def selection_sort(arr: list[int | float]) -> list[int | float]:
    length = len(arr)
    for i in range(length):
        min_num_index = i
        for j in range(i + 1, length):
            if arr[min_num_index] > arr[j]:
                min_num_index = j
        arr[min_num_index], arr[i] = arr[i], arr[min_num_index]
    return arr