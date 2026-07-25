class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)

        if n + m != len(s3):
            return False

        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == n and j == m:
                return True

            k = i + j
            res = False

            if i < n and s1[i] == s3[k]:
                res = res or dp(i + 1, j)

            if j < m and s2[j] == s3[k]:
                res = res or dp(i, j + 1)

            memo[(i, j)] = res
            return res

        return dp(0, 0)