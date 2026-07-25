from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0

        res = 1
        freq = defaultdict(int)
        for r in range(len(s)):
            freq[s[r]] += 1
            while l < r and freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res

