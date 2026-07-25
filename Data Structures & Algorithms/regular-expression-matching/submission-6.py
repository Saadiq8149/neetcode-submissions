class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        memo = {}
        def dp(i=0, j=0):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == n and j == m:
                return True
            if j == m:
                return False

            if j < m-1 and p[j+1] == "*":
                skip = dp(i, j + 2)
                use  = (i < n and (p[j] == "." or p[j] == s[i])) and dp(i + 1, j)
                memo[(i, j)] = skip or use
            else:
                if i < n and (p[j] == "." or p[j] == s[i]):
                    memo[(i, j)] = dp(i + 1, j + 1)
                else:
                    memo[(i, j)] = False
            return memo[(i, j)]

        return dp()