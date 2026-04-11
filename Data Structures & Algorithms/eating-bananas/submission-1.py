import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            mid = (l+r) // 2

            tot_hrs = 0
            for pile in piles:
                tot_hrs += math.ceil(pile/mid)
            
            if tot_hrs <= h:
                r = mid
            else:
                l = mid + 1

        return l
