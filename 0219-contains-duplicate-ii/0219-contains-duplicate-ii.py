# USING HASHMAP -> MY SOLN
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index, num in enumerate(nums):
            if num in d and abs((d[num] - index)) <= k:
                return True
            d[num] = index
        return False

################################
# USING SLIDING WINDOW -> NEETCODE SOLN
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            if abs(R - L) > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
