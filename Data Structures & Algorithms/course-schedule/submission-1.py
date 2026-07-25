class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            map[c].append(p)

        visited = set()

        def dfs(c):
            if c in visited:
                return False

            if len(map[c]) == 0:
                return True

            visited.add(c)
            for n in map[c]:
                if not dfs(n):
                    return False
            visited.remove(c)
            # map[c] = []
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True