class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        memo = {}
        def dp(curr, pos):
            if (curr,pos) in memo:
                return memo[(curr, pos)]

            if curr == 0:
                return 1
            elif curr < 0:
                return 0
            
            ways = 0
            for i in range(pos, n):
                ways += dp(curr-coins[i], i)

            memo[(curr, pos)] = ways
            return ways

        return dp(amount, 0)