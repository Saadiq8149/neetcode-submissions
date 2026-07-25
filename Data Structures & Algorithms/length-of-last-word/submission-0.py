class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        s = [i for i in s if i.strip() != ""]

        return len(s[-1])