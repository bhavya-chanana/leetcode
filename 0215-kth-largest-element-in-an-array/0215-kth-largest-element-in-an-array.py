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
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k = len(nums) - k
        def quickSelect(left, right):
            pivot, p = nums[right], left
             
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[right] = nums[right], nums[p]

            if p > self.k: return quickSelect(left, p - 1)
            elif p < self.k: return quickSelect(p + 1, right)
            else: return nums[p]

        return quickSelect(0, len(nums) - 1)
