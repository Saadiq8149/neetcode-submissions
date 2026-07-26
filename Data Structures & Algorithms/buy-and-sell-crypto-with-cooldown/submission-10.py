class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, canBuy):
            if i >= len(prices):
                return 0

            if (i, canBuy) in memo:
                return memo[(i, canBuy)]

            if canBuy:
                ans = max(
                    dfs(i + 1, False) - prices[i],  
                    dfs(i + 1, True)                 
                )
            else:
                ans = max(
                    dfs(i + 2, True) + prices[i],    
                    dfs(i + 1, False)                
                )

            memo[(i, canBuy)] = ans
            return ans

        return dfs(0, True)
