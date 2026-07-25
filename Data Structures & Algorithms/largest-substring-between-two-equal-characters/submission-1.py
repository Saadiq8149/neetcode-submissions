class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mpp = {}
        for i, c in enumerate(s):
            if c in mpp:
                mpp[c].append(i)
            else:
                mpp[c] = [i]

        res = -1
        for k, v in mpp.items():
            if len(v) > 1:
                res = max(res, v[-1] - v[0] - 1)

        return res
