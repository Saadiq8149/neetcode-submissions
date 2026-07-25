class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in adj[node]:
                dfs(n)

        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1

        return components
