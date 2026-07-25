class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        
        def recurse(i, rem):
            res = 0
            if (i, rem) in memo:
                return memo[(i, rem)]

            if rem == 0:
                return 1

            if i >= len(coins) or rem < 0:
                return 0

            rem -= coins[i]
            res += recurse(i, rem)
            rem += coins[i]
            res += recurse(i+1, rem)

            memo[(i, rem)] = res 

            return res

        return recurse(0, amount)
            
