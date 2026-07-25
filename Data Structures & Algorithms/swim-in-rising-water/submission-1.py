class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        min_heap = [(grid[0][0], 0, 0)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while min_heap:
            cost, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue
            visited.add((r, c))

            if r == n - 1 and c == n - 1:
                return cost

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    new_cost = max(cost, grid[nr][nc]) 
                    heapq.heappush(min_heap, (new_cost, nr, nc))