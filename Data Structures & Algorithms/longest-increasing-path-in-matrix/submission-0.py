class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        memo = {}

        def dfs(r, c, prevVal):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or matrix[r][c] <= prevVal:
                return 0

            if (r, c) in memo:
                return memo[(r, c)]

            res = 1
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                res = max(res, 1 + dfs(nr, nc, matrix[r][c]))

            memo[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)

        return max(memo.values())


            