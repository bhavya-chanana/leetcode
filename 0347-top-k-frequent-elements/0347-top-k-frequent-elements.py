class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for i in nums:
            d[i]=d.get(i, 0) + 1
        m = sorted(d.values(), reverse=True)[k-1]
        for key in d:
            if d[key]>=m: 
                l.append(key)
        return l
