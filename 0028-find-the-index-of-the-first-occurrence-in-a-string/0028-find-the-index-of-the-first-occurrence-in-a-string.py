### both soln have same time complexity --- O(m * n)
#using string manipulation 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i 
        return -1   


# using nested for loops
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for index in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[index + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return index
        return -1   
