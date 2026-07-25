class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s),len(t)

        memo = {}
        def dp(l=0, p=0):
            if (l, p) in memo:
                return memo[(l, p)]

            if l == m:
                return 1

            if p == n:
                return 0

            if s[p] == t[l]:
                memo[(l, p)] = dp(l+1, p+1) + dp(l, p+1)
            else:
                memo[(l ,p)] = dp(l, p+1)
            return memo[(l, p)]

        return dp()
