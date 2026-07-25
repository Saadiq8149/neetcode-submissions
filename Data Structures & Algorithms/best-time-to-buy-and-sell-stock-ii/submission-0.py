class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        cache = {}

        def dp(i=0, bought=False):
            if (i, bought) in cache:
                return cache[(i, bought)]

            if i == len(prices):
                return 0

            res = dp(i+1, bought)
            if bought:
                res = max(res, prices[i] + dp(i+1, False))
            else:
                res = max(res, -prices[i] + dp(i+1, True))

            cache[(i, bought)] = res
            return res

        return dp()
            
            

