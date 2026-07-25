class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0

        row = 1
        while n >= 0:
            n -= row
            rows += 1
            row += 1

        return rows-1