from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w = len(s1)

        if w > len(s2):
            return False

        req = Counter(s1)
        window = Counter(s2[:w])

        if window == req:
            return True

        for r in range(w, len(s2)):
            window[s2[r]] += 1
            window[s2[r - w]] -= 1

            if window == req:
                return True

        return False