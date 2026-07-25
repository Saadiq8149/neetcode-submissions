class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        res = 1
        maxFreq = 1

        l = 0

        for r in range(len(s)):
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])

            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res