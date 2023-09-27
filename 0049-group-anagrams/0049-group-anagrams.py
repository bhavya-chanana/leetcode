class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list) 
        for s in strs:
            count = [0] * 26    #array for storing count of a...z

            for c in s:
                count[ord(c) - ord('a')] += 1
                
            res[tuple(count)].append(s) 
            
        return res.values()
