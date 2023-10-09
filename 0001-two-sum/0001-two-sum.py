class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            rem = target - num
            if rem in d:
                return [d[rem], index]
            d[num] = index