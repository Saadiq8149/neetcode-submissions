class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        for c in s:
            if c == "1":
                ones += 1

        res = ""
        for _ in range(ones-1):
            res += "1"
        for _ in range(len(s) - ones):
            res += "0"
        res += "1"
        return res

