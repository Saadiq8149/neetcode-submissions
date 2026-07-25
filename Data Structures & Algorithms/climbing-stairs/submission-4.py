class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def recurse(i):
            if i in memo:
                return memo[i]

            if i<= 2:
                return i

            memo[i] = recurse(i-1) + recurse(i-2)
            return memo[i]

        return recurse(n)