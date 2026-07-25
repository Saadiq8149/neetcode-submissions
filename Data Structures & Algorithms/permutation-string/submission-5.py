from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w = len(s1)

        if w > len(s2):
            return False

        need = Counter(s1)
        window = Counter(s2[:w])

        if window == need:
            return True

        for r in range(w, len(s2)):
            window[s2[r]] += 1

            left = s2[r - w]
            window[left] -= 1

            if window[left] == 0:
                del window[left]

            if window == need:
                return True

        return False