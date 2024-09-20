class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        maxheap = [-i for i in stones]
        heapq.heapify(maxheap)
        print(maxheap)

        while len(maxheap) > 1:
            y = -heappop(maxheap)
            x = -heappop(maxheap)
            y = y - x
            if y != 0:
                heappush(maxheap, -y)
            

        if maxheap:
            return -maxheap[0]
        return 0
        
        
