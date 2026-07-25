class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mpp = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            mpp[tuple(freq)].append(word)

        res = []
        for v in mpp.values():
            res.append(v)

        return res