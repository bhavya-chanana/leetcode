class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        maxSum = k * threshold
        l = 0
        s = sum(arr[:k])
        count = 0
        for r in range(k, len(arr)):
            if s >= maxSum:
                count += 1
            s = s - arr[l]
            l += 1
            s = s + arr[r]
        
        if s >= maxSum:
            count += 1

        return count

            