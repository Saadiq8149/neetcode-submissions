class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pos = 0
        common = ""
        while True:
            if pos >= len(strs[0]):
                return common

            c = strs[0][pos]
            for s in strs:
                if pos >= len(s) or c != s[pos]:
                    return common
                
            common += c
            pos += 1
        
        return common