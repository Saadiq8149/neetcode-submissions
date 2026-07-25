class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)

        def dp(i):
            if i >= n:
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = cost[i] + min(dp(i+1), dp(i+2))
            return cache[i]
        
        return min(dp(0), dp(1))