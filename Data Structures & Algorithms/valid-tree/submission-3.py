class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        map = {i : [] for i in range(n)}

        for e in edges:
            map[e[0]].append(e[1])
            map[e[1]].append(e[0])

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for n in map[node]:
                if n == parent:
                    continue

                if not dfs(n, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n

