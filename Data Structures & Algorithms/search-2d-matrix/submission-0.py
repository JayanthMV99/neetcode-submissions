class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = n * m - 1

        while l <= r:
            mid = l + (r - l) // 2
            midValue = matrix[mid // n][mid % n]

            if midValue == target:
                return True
            if midValue > target:
                r = mid - 1
            else:
                l = mid + 1

        return False