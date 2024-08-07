class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != '*':
                stack.append(char)
                continue
            stack.pop(-1)

        return ''.join(stack)