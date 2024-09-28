class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        q = deque() # [-c, idleTime]
        time = 0

        while maxHeap or q:
            time += 1
            
            if maxHeap:
                c = 1 + heapq.heappop(maxHeap) # 1 + (-ve value) 
            
                if c != 0:
                    q.append([c, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0]) # push -c (popped value) to the heap
            
        return time
