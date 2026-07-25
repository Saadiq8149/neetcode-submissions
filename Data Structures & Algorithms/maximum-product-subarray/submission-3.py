class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]

        for i in range(n):
            if i == 0:
                dp[i] = [nums[i], nums[i]]
                continue

            dp[i][0] = max(nums[i], dp[i-1][0]*nums[i], dp[i-1][1]*nums[i])
            dp[i][1] = min(nums[i], dp[i-1][0]*nums[i], dp[i-1][1]*nums[i])

        result = dp[0][0]
        for d in dp:
            result = max(result, d[0], d[1])

        return result