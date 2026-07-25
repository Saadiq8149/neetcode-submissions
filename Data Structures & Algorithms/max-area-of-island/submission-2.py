class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, area):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0

            return 1 + dfs(r, c+1, area) + dfs(r, c-1, area) + dfs(r+1, c, area) + dfs(r-1, c, area)

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c, 1))

        return maxArea


