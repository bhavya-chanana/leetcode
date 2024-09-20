class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for x, y in points:
            distance = x** 2 + y ** 2
            res.append({'coord': [x, y], 'distance': distance})

        heap = (heapq.nsmallest(k, res, key = lambda r: r['distance']))

        return [i['coord'] for i in heap]