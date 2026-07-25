class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mpp = defaultdict(int)

        for i, c in enumerate(s):
            mpp[c] = max(mpp[c], i)

        print(mpp)

        res = []
        l = 0
        end = mpp[s[0]]
        for i in range(len(s)):
            end = max(end, mpp[s[i]])
            if i == end:
                res.append(i - l + 1)
                l = i + 1
        
        return res
            