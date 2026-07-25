class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = [[] for _ in range(n+1)]
        visited = [False] * (n + 1)
        cycle = set()
        cycleStart = -1

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        def dfs(curr, prev):
            nonlocal cycleStart
            if visited[curr]:
                cycleStart = curr
                return True
            
            visited[curr] = True
            for n in adj[curr]:
                if n == prev:
                    continue
                if dfs(n, curr):
                    if cycleStart != -1:
                        cycle.add(curr)
                    if curr == cycleStart:
                        cycleStart = -1
                    return True

            return False
        
        dfs(1, -1)

        for a,b in reversed(edges):
            if a in cycle and b in cycle:
                return [a, b]

        return []

