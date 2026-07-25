class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visiting = set()

        def dfs(curr, prev):
            # print(visiting, curr, prev)
            if curr in visiting:
                return False

            visiting.add(curr)
            for n in adj[curr]:
                if prev is not None and n == prev:
                    continue
                if not dfs(n, curr):
                    return False
            visiting.remove(curr)
            visited.add(curr)
            return True

        for n in adj:
            visited = set()
            if not dfs(n, None) or len(visited) < n:
                return False
        
        return True