from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, curr):
            if (i, curr) in memo:
                return memo[(i, curr)]

            if i == len(coins) or curr > amount:
                return 0

            if curr == amount:
                return 1

            take = dfs(i, curr+coins[i])
            skip = dfs(i+1, curr)
            memo[(i, curr)] = take + skip
            return take + skip

        return dfs(0, 0)
