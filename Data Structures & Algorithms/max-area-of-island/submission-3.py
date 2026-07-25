class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        maxArea = 0
        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            area = 0            
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                area += dfs(dr+r, dc+c)
            
            return area + 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(dfs(r, c), maxArea)

        return maxArea