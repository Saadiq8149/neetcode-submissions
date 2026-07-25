class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        s1_freq = [0] * 26
        for ch in s1:
            s1_freq[ord(ch) - ord('a')] += 1

        s2_freq = [0] * 26
        l = 0

        for r in range(m):
            s2_freq[ord(s2[r]) - ord('a')] += 1

            if (r - l + 1) > n:
                s2_freq[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if (r - l + 1) == n:
                if s1_freq == s2_freq:
                    return True

        return False
