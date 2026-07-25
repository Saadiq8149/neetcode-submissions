from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        length = 1
        freq = defaultdict(int)

        l, r = 0, 0
        freq[s[0]] += 1

        while r < len(s):
            length = max(length, r-l+1)
            while l <= r and r < len(s)-1 and freq[s[r+1]] > 0:
                freq[s[l]] -= 1
                l += 1

            if r < len(s) - 1:
                freq[s[r+1]] += 1
            r += 1

        return length

