class Solution:
    def tribonacci(self, n: int) -> int:
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(1)

        for n in range(3, n+1):
            dp.append(dp[n-1] + dp[n-2] + dp[n-3])

        return dp[n]