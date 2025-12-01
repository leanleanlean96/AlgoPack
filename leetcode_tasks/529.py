class Solution:
    def fib(self, n: int) -> int:
        prev: int = 0
        curr: int = 1
        if n == 0:
            return 0
        for i in range(n - 1):
            prev, curr = curr, prev + curr
        return curr