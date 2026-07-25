class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False 

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)
        count = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1

        directions = [(1, 0), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    idx = r * cols + c

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                            nidx = nr * cols + nc
                            if uf.union(idx, nidx):
                                count -= 1

        return count


