def countingSort(arr):
    nums_count: list[int] = [0] * 100
    current_ind: int = 0
    for num in arr:
        nums_count[num] += 1
    for i in range(100):
        for j in range(nums_count[i]):
            arr[current_ind] = i
            current_ind += 1
    return arr