class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        profit = 0

        for b in range(n-1):
            for s in range(b+1, n):
                profit = max(profit, prices[s]-prices[b])

        return profit