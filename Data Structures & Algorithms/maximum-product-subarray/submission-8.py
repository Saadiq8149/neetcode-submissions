class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        curMax, curMin = 1, 1

        for n in nums:
            temp = curMax * n

            curMax = max(curMax * n, n, n * curMin)
            curMin = min(temp, n, n * curMin)
            res = max(res, curMax)

        return res