class Solution:
    def countBits(self, n: int) -> List[int]:
        op = [0] * (n+1)

        for i in range(0, n+1):
            op[i] = op[i>>1] + (i&1)

        return op