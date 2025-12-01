def counting_sort(arr: list[int]):
    nums = [0] * (max(arr) + 1)
    sorted_array = [None] * len(arr)

    for num in arr:
        nums[num] += 1
    for ind in range(1, len(nums)):
        nums[ind] += nums[ind - 1]
    for i in range(len(arr) - 1, -1, -1):
        sorted_array[nums[arr[i]] - 1] = arr[i]
        nums[arr[i]] -= 1

    return sorted_array