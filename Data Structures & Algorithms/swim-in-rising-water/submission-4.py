class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]        
        dist[0][0] = grid[0][0]

        min_heap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while min_heap:
            curr_dist, r, c = heapq.heappop(min_heap)

            if (r, c) == (rows-1, cols-1):
                return curr_dist

            if curr_dist > dist[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                new_dist = max(curr_dist, grid[nr][nc])

                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(min_heap, (new_dist, nr, nc))

        return -1