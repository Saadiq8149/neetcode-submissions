class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        
        pos = 0
        while pos < len(word1) and pos < len(word2):
            new += word1[pos]
            new += word2[pos]
            pos += 1

        if pos < len(word1):
            new += word1[pos:]
        else:
            new += word2[pos:]

        return new
