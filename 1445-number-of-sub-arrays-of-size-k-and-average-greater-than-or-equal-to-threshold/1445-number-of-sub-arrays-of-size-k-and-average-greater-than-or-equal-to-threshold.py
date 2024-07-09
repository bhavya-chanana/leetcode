class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1
        maxSum = k * threshold
        window = []
        s = 0
        count = 0
        for r in range(len(arr)):
            if len(window) == k:
                if s >= maxSum:
                    count += 1
                s = s - window[0]
                window.pop(0)
            
            if len(window) < k:
                s = s + arr[r]
                window.append(arr[r])

        s = sum(window)
        if s >= maxSum:
            count += 1

        return count

            