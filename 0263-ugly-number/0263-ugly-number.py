class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1: return True
        ugly = [2, 3, 5]
        
        for num in ugly:
            while n > 1 and n % num == 0:
                n = n // num
        return n == 1
