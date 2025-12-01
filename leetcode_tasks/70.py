class Solution:
    def climbStairs(self, num: int) -> int:
        if num <= 3:
            return num
        num_minus_2: int = 1
        num_minus_1: int = 1
        for i in range(num - 1):
            num_minus_2, num_minus_1 = num_minus_1, num_minus_1 + num_minus_2
        return num_minus_1