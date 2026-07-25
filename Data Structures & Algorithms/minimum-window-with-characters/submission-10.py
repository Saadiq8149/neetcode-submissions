class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)

        l = 0
        window = defaultdict(int)
        found = 0
        
        resIdx = [None, None]

        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in tCount and window[s[r]] <= tCount[s[r]]:
                found += 1

            while found == len(t):
                if resIdx[0] is None or resIdx[1] is None or (resIdx[1] - resIdx[0]) > (r - l):
                    resIdx = [l, r]
                if s[l] in tCount and window[s[l]] <= tCount[s[l]]:
                    found -= 1
                window[s[l]] -= 1
                l += 1


        if resIdx[0] is None or resIdx[1] is None:
            return ""
        return s[resIdx[0]:resIdx[1]+1]



            


        

            