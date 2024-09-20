class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            distance = (x - 0) ** 2 + (y - 0) ** 2
            res.append({'coord': [x, y], 'distance': distance})

        heap = (heapq.nsmallest(k, res, key = lambda r: r['distance']))
        result = []
        for i in heap:
            result.append(i['coord'])

        return result