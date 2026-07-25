class Solution:
    def maxDepth(self, s: str) -> int:
        curr = 0
        res = 0

        for c in s:
            if c == "(":
                curr += 1
            elif c == ")":
                res = max(curr, res)
                curr -= 1

        return res