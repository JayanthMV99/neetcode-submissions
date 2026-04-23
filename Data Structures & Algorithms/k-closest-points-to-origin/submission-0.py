class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x,y in points:
            dist = x * x + y * y
            minHeap.append((dist, [x,y]))

        heapq.heapify(minHeap)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res