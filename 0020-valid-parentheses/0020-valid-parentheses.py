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
            