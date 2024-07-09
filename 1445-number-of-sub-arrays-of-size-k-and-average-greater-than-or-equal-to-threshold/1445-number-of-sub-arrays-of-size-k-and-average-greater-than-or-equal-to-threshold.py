class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        maxSum = k * threshold
        l = 0
        currSum = sum(arr[:k])
        count = 0
        for r in range(k, len(arr)):
            if currSum >= maxSum:
                count += 1
            currSum = currSum - arr[l]
            l += 1
            currSum = currSum + arr[r]
        
        if currSum >= maxSum:
            count += 1

        return count

            