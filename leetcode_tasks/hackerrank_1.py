def countingSort(arr):
    nums_count: list[int] = [0] * 100
    for num in arr:
        nums_count[num] += 1
    return nums_count