class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heappop(self.minheap)
        return self.minheap[0]
       
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)