class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        visited = set()
        def dfs(curr):
            if curr in visited:
                return False
            
            visited.add(curr)
            for n in adj[curr]:
                if n in visited:
                    continue
                if not dfs(n):
                    return False
            return True

        res = 0
        for n in adj:
            if dfs(n):
                res += 1

        return res     

