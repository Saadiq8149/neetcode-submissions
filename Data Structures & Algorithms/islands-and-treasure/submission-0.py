class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        length = 0
        while q:
            row, col = q.popleft()
            length += 1

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == -1:
                    continue

                if grid[nr][nc] == 2147483647:
                    grid[nr][nc] = 1 + grid[row][col]
                    q.append((nr, nc))

