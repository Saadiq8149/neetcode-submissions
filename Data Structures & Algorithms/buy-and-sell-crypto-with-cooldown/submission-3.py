class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def dp(i=0, profit=0, canBuy=True, memo={}):
            state = str(i)+","+str(canBuy)
            if state in memo:
                return memo[state]

            if (i == n-1 and canBuy) or i >= n:
                return profit

            if canBuy:
                # Buy or Skip
                memo[state] = max(
                    -prices[i] + dp(i+1, profit, False, memo),
                    dp(i+1, profit, canBuy, memo)
                )
            else:
                # Sell or Skip
                memo[state] = max(
                    prices[i] + dp(i+2, profit, True, memo),
                    dp(i+1, profit, canBuy, memo)
                )
            return memo[state]

        return dp()