class Solution:
    
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def getNeighbours(r, c):
            n = []
            if r > 0:
                n.append((grid[r-1][c], (r-1, c)))
            if c > 0:
                n.append((grid[r][c-1], (r, c-1)))
            if r < ROWS - 1:
                n.append((grid[r+1][c], (r+1, c)))
            if c < COLS - 1:
                n.append((grid[r][c+1], (r, c+1)))
            return n
        

        adj = defaultdict(list)
        for r in range(ROWS):
            for c in range(COLS):
                adj[(r, c)].extend(getNeighbours(r, c))


        shortest = {}
        heap = [(grid[0][0], (0, 0))]
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for w2, n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(heap, (max(w2, w1), n2))

        return shortest[(ROWS-1, COLS-1)]

