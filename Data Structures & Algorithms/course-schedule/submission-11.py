class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for p in prerequisites:
            adj[p[0]].append(p[1])

        visiting = set()

        def dfs(curr):
            if curr in visiting:
                return False
            if adj[curr] == []:
                return True

            visiting.add(curr)
            for pre in adj[curr]:
                if not dfs(pre):
                    return False
            visiting.remove(curr)
            adj[curr] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True