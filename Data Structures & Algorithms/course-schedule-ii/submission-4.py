class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj[crs].append(pre)

        res = []
        cycle = set()
        visited = set()
        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visited:
                return True

            cycle.add(curr)
            for pre in adj[curr]:
                if not dfs(pre):
                    return False
            cycle.remove(curr)
            visited.add(curr)
            res.append(curr)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res