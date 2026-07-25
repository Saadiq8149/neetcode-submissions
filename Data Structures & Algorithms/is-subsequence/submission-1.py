class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
                
        start = 0
        for c1 in s:
            found = False
            for i in range(start, len(t)):
                if c1 == t[i]:
                    found = True
                    start = i+1
                    break

            if not found:
                return False

        return True
            