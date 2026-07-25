class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp = {}

        for s in strs:
            freq = [0 for i in range(26)]
            for c in s:
                freq[ord(c)-ord('a')] += 1
            
            key = str(freq)
            if key in mpp:
                mpp[key].append(s)
            else:
                mpp[key] = [s]

        result = []
        for k in mpp:
            result.append(mpp[k])

        return result