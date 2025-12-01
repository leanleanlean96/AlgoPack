def factorial_recursive(num: int, factorial_hash: dict[int, int] = None) -> int:
    if num < 0:
        return -1
    if factorial_hash is None:
        factorial_hash = {0: 1, 1: 1}
    if num in factorial_hash:
        return factorial_hash[num]
    factorial_hash[num] = factorial_recursive(num - 1, factorial_hash) * num
    return factorial_hash[num]

def factorial_dynamic(num: int) -> int:
    if num < 0:
        return -1
    if num == 0:
        return 1
    for i in range(1, num):
        num *= i
    return num