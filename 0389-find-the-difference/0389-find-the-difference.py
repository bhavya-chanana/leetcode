class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for i in s:
            d[i]=d.get(i, 0) + 1
        for i in t:
            # if d.get(i):
            #     d[i] = d[i] - 1
            # else:
            #     return i
            d[i] = d.get(i, 0) - 1
            if d[i] == -1:
                return i
            