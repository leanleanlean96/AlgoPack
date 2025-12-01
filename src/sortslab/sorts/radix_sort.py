def counting_sort(arr: list[int], current_digit: int, base: int):
    nums = [0] * base
    sorted_arr = [0] * len(arr)
    for num in arr:
        index = (num // current_digit) % base
        nums[index] += 1

    for i in range(1, base):
        nums[i] += nums[i - 1]

    for num in reversed(arr):
        index = (num // current_digit) % base
        nums[index] -= 1
        sorted_arr[nums[index]] = num
        
        
    return sorted_arr

def radix_sort(arr: list[int], base: int = 10) -> list[int]:
    max_num: int = max(arr)
    current_digit: int = 1
    while max_num // current_digit > 0:
        arr = counting_sort(arr, current_digit, base)
        current_digit *= base
    return arr