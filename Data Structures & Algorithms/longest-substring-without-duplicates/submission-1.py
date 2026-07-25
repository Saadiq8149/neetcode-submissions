class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        chars = {s[0]: 0}

        maxL = 1
        l = 0
        
        for r in range(1, len(s)):
            
            if s[r] in chars and chars[s[r]] >= l:
                l = chars[s[r]] + 1 
                chars[s[r]] = r
            else:
                chars[s[r]] = r

            length = r - l + 1
            maxL = max(maxL, length)

        return maxL
