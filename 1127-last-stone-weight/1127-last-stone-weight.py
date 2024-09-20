class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        maxheap = [-i for i in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            y = heappop(maxheap)
            x = heappop(maxheap)
            
            if y != x:
                heappush(maxheap, y-x)

        if maxheap:
            return -maxheap[0]
        return 0
        
        
