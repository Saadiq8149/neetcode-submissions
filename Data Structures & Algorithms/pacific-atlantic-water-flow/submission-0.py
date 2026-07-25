class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        ROWS, COLS = len(heights), len(heights[0])
        
        atl = set()
        pcf = set()

        a = deque()
        
        # atl
        for c in range(COLS):
            a.append((ROWS-1, c))
            atl.add((ROWS-1, c))
        for r in range(ROWS):
            a.append((r, COLS-1))
            atl.add((r, COLS-1))

        while a:
            row, col = a.popleft()

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                nr, nc = row+dr, col+dc

                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS:
                    continue

                if (nr, nc) not in atl and heights[nr][nc] >= heights[row][col]:
                    atl.add((nr, nc))
                    a.append((nr, nc))

        p = deque()
        
        # pcf
        for c in range(COLS):
            p.append((0, c))
            pcf.add((0, c))
        for r in range(ROWS):
            p.append((r, 0))
            pcf.add((r, 0))

        while p:
            row, col = p.popleft()

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                nr, nc = row+dr, col+dc

                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS:
                    continue

                if (nr, nc) not in pcf and heights[nr][nc] >= heights[row][col]:
                    pcf.add((nr, nc))
                    p.append((nr, nc))

        for x in atl:
            if x in pcf:
                result.append([x[0], x[1]])

        return result

