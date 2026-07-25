class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for p in prerequisites:
            adj[p[0]].append(p[1])

        visited = set()

        def dfs(curr):
            if curr in visited:
                return False
            if adj[curr] == []:
                return True

            visited.add(curr)
            for pre in adj[curr]:
                if not dfs(pre):
                    return False
            visited.remove(curr)
            adj[curr] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True