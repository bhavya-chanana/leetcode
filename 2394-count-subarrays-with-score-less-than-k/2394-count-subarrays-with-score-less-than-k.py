class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        count = 0
        n = len(nums)
        prefix = 0
        for r in range(n):
            prefix += nums[r]
            while prefix * (r - l + 1) >= k:
                prefix -= nums[l]
                l += 1
            count += (r - l + 1)
        
        return count