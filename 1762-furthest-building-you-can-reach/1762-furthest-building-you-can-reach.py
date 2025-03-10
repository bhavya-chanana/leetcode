class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff > 0:
                heapq.heappush(minHeap, diff)

                if len(minHeap) > ladders:
                    bricks -= heapq.heappop(minHeap)
                
                if bricks < 0:
                    return i
        
        return len(heights) - 1

                                                                                                                              