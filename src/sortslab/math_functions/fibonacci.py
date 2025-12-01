def fibo_recursive(num: int, fibo_hash: dict[int, int] = None) -> int:
    if fibo_hash is None:
        fibo_hash: dict[int, int] = {0: 0, 1: 1}
    if num in fibo_hash:
        return fibo_hash[num]
    if num - 1 not in fibo_hash:
        fibo_recursive(num - 1, fibo_hash)
    fibo_hash[num] = fibo_hash[num - 1] + fibo_hash[num - 2]
    return fibo_hash[num]

def fibo_dynamic(num: int) -> int:
    if num == 0:
        return 0
    if num <= 2:
        return 1
    num_minus_2 = 1
    num_minus_1 = 1
    for i in range(num - 2):
        num_minus_2, num_minus_1 = num_minus_1, num_minus_1 + num_minus_2
    return num_minus_1