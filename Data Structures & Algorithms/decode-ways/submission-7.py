class Solution:

    def numDecodings(self, s: str) -> int:
        def dp(s, memo={}):
            if s in memo:
                return memo[s]
            if s == "":
                return 1
            if s[0] == "0":
                return 0
            if len(s) == 1:
                return 1
            
            memo[s] = 0

            memo[s] += dp(s[1:])
            if int(s[0:2]) <= 26:
                memo[s] += dp(s[2:])

            return memo[s]

        return dp(s)