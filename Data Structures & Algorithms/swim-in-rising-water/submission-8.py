class Solution:
    
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])        

        shortest = {}
        heap = [(grid[0][0], (0, 0))]
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in shortest:
                continue
            r, c = n1
            shortest[n1] = w1

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = dr + r, dc + c
                if min(nr, nc) < 0 or nr >= ROWS or nc >= COLS or (nr, nc) in shortest:
                    continue
                heapq.heappush(heap, (max(grid[nr][nc], w1), (nr, nc)))

        return shortest[(ROWS-1, COLS-1)]

