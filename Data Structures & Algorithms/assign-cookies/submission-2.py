class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        okay = 0

        for i in range(len(g)):
            for j in range(len(s)):
                if s[j] >= g[i]:
                    okay += 1
                    s[j] = -1
                    break

        return okay