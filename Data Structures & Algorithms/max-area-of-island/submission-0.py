from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [0] * n 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
            self.size[ry] += self.size[rx]
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
            self.size[rx] += self.size[ry]
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
            self.size[rx] += self.size[ry]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    uf.size[r * cols + c] = 1

        directions = [(1, 0), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    idx = r * cols + c
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            uf.union(idx, nr * cols + nc)

        return max(uf.size)
