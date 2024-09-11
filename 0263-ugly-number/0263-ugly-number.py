class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        ugly = [2, 3, 5]
        
        for num in ugly:
            while n % num == 0:
                n = n // num
        return n == 1
