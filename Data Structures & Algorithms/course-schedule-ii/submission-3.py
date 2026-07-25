class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            graph[c].append(p)

        visiting = set()
        visited = set()
        output = []

        def dfs(c):
            if c in visiting:
                return False

            if c in visited:
                return True

            visiting.add(c)

            for pre in graph[c]:
                if not dfs(pre):
                    return False

            visiting.remove(c)
            visited.add(c)
            output.append(c)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return output