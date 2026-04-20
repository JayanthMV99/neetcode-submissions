class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        op = [0] * len(temp)
        stack = []

        for i in range(len(temp)):
            while len(stack) != 0 and temp[i] > temp[stack[-1]]:
                idx = stack.pop()
                op[idx] = i -idx
            stack.append(i)

        return op