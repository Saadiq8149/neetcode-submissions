class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        
        seen = 0
        total = len(t)
        res = float('inf')
        resIdx = [None, None]

        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in tCount:
                if tCount[c] > 0:
                    seen += 1
                tCount[c] -= 1
            print(tCount, seen)

            while seen == total:
                if r - l + 1 <= res:
                    resIdx[0] = l
                    resIdx[1] = r
                    res = r - l + 1

                lC = s[l]
                if lC in tCount:
                    tCount[lC] += 1
                    if tCount[lC] > 0:
                        seen -= 1
                l += 1

        if res == float('inf'):
            return ""

        return s[resIdx[0]:resIdx[1]+1]

        

            