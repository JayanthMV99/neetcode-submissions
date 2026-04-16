class Solution:
    def countBits(self, n: int) -> List[int]:
        op = []

        for i in range(0, n+1):
            cnt = 0
            while i:
                i = i & (i - 1)
                cnt += 1
            op.append(cnt)

        return op