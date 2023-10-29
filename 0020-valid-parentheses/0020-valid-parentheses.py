class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if(top == '[' and i != ']') or (top == '(' and i != ')') or (top == '{' and i != '}'):
                    return False
                else:
                    stack.pop()
        
        return True if not stack else False


class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
            
