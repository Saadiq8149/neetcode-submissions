class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from functools import cache
        @cache
        def backtrack(i, curr):
            if curr == amount:
                return 1
            if i >= len(coins) or curr > amount:
                return 0

            res = 0

            res += backtrack(i, curr+coins[i])
            while i+1 < len(coins) and coins[i+1] == coins[i]:
                i += 1
            res += backtrack(i+1, curr)
            return res

        return backtrack(0, 0)