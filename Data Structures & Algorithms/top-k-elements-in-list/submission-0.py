class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        freqs = [[] for _ in range(len(nums)+1)]
        for num, cnt in counts.items():
            freqs[cnt].append(num)

        res = []
        for i in range(len(freqs)-1, 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res