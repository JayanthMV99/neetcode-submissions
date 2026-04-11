class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        op = nums[0]

        if len(nums) == 0:
            return op

        while l <= r:
            if nums[l] < nums[r]:
                op = min(op, nums[l])

            mid = (l+r) // 2
            op = min(op, nums[mid])

            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return op