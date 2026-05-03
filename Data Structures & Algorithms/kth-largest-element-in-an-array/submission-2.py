class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        for _ in range(k):
            op = -heapq.heappop(maxHeap)

        return op