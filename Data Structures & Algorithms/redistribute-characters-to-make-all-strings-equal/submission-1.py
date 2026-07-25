class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = defaultdict(int)

        for w in words:
            for c in w:
                freq[c] += 1

        for k, v in freq.items():
            if v % len(words) != 0:
                return  False

        return True
