class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list) #makes an new empty list when there key aint there rather than raising keyError
        for s in strs:
            count = [0] * 26    #array for storing count of a...z

            for c in s:
                count[ord(c) - ord('a')] += 1
                
            res[tuple(count)].append(s) #converted count list to tuple as python doesnt accept list as keys
        return res.values()
