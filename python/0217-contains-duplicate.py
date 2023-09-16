# question - https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

# u can also add all the values to hashset and compare the size of hashset and nums
# as hashset doesnt allow duplicate values therefore if the size of hashset < size of nums: return true contains duplicate