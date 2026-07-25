class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        ROWS, COLS = len(grid), len(grid[0])
       
        q = deque()
        q.append((0, 0))
        visited = set()
        length = 0

        while q:
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length + 1

                visited.add((r, c))

                for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
                    nr, nc = r + dr, c + dc

                    if (nr, nc) in visited or min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 1:
                        continue
                    q.append((nr, nc))

            length += 1

        return -1
