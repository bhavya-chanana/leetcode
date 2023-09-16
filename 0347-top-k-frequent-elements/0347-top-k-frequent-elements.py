## u take the values and sort it in decreasing order and target the k-1 element in that sorted array as that is the threshold freq/value and append those keys to a list 
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


## u sort the whole dict using value in decreasing order and print the first k elements 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l = []
        for i in nums:
            d[i]=d.get(i, 0) + 1
        sorted_d = sorted(d.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            l.append(sorted_d[i][0])
        return l
