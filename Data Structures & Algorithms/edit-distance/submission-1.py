class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)

        memo = {}
        def dp(i=0, j=0):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == n:
                return m - j

            if j == m:
                return n - i

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i+1, j+1)
            else:
                # insert: i, j+1
                # delete: i+1, j
                # replace: i+1, j+1
                res = min(dp(i,j+1), dp(i+1, j))
                res = min(res, dp(i+1, j+1))
                memo[(i, j)] = res+1
            return memo[(i, j)]

        return dp()

            

