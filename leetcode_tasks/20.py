class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[int] = []
        parenthesis_dict: dict[str, str] = {")": "(",
                            "}": "{",
                            "]": "["}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or stack.pop() != parenthesis_dict[char]:
                    return False
        if stack:
            return False
        return True