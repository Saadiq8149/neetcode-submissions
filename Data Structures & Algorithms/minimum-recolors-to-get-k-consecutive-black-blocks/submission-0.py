class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        window = {
            "W": 0,
            "B": 0
        }
        for i in range(k):
            window[blocks[i]] += 1
        res = window["W"]
        
        l = 0
        for r in range(k, n):
            res = min(res, window["W"])
            window[blocks[l]] -= 1
            window[blocks[r]] += 1
            l += 1

        return res

        