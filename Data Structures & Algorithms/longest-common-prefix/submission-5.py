class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        common = 0

        run = True
        while run:
            for s in strs:
                if common >= len(s) or not s[common] == strs[0][common]:
                    run = False
                    break
            if run:
                common += 1

        return strs[0][:common]