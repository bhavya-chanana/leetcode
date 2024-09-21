## Soln 1 - using sorting - O(N) = N logN
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        return(nums[k - 1])

## Soln 2 - using minHeap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in  nums:
            heappush(minHeap, num)
            if len(minHeap) > k:
                heappop(minHeap)
            print(minHeap)

        return abs(minHeap[0]) 

## Soln 3 - using quickSelect algorithm - 
# O(n) = N -> average case
# O(n) = N^2 -> worst case
