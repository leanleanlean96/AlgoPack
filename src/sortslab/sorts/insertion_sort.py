def insertion_sort(arr: list[int | float]) -> list[int | float]:
    for ind in range(1, len(arr)):
        prev_ind = ind
        while prev_ind > 0 and arr[prev_ind - 1] > arr[prev_ind]:
            arr[prev_ind], arr[prev_ind - 1] = arr[prev_ind - 1], arr[prev_ind]
            prev_ind -= 1
    return arr