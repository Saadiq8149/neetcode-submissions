from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, curr):
            if i == len(coins) or curr > amount:
                return 0

            if curr == amount:
                return 1

            take = dfs(i, curr+coins[i])
            skip = dfs(i+1, curr)
            return take + skip

        return dfs(0, 0)
