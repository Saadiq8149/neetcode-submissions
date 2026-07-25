class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS, INF = len(grid), len(grid[0]), 2147483647
        
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != INF:
                    continue
                q.append((nr, nc))
                grid[nr][nc] = grid[r][c] + 1



