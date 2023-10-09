class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index, num in enumerate(nums):
            if num in d:
                if abs((d[num] - index)) <= k:
                    return True
            d[num] = index
        return False