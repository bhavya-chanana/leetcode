class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = {}
        countS2 = {}

        for i in s1:
            countS1[i] = countS1.get(i, 0) + 1
        
        l = 0
        for r in range(len(s2)):
            countS2[s2[r]] = countS2.get(s2[r], 0) + 1

            while (r - l + 1) > (len(s1)):
                countS2[s2[l]] -= 1
                if countS2[s2[l]] == 0:
                    countS2.pop(s2[l])

                l += 1

            if countS1 == countS2:
                return True
        
        return False
