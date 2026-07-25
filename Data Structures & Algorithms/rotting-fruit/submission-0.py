class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        fresh = 0
        time = 0

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            row, col, t = q.popleft()      
            time = max(time, t)

            for dr, dc in DIRECTIONS:
                nr = row + dr
                nc = col + dc

                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                    continue

                if grid[nr][nc] == 1:
                    fresh -= 1
                    grid[nr][nc] = 2
                    q.append((nr, nc, t+1))

        return time if fresh == 0 else -1


