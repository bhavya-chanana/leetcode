class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        p1 = 0
        p2 = len(s) - 1
        for i in range(len(s)//2):
            if s[p1] != s[p2]:
                return False
            p1 = p1 + 1
            p2 = p2 - 1
            continue
        return True
