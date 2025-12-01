class Solution:
    def sortColors(self, nums: list[int]) -> None:
        colors_count: list[int] = [0] * 3
        current_ind: int = 0
        for num in nums:
            colors_count[num] += 1
        for i in range(1, len(colors_count)):
            colors_count[i] += colors_count[i - 1]
        for color in range(len(colors_count)):
            while current_ind < colors_count[color]:
                nums[current_ind] = color
                current_ind += 1
        