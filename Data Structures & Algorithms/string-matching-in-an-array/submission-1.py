class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        
        for w1 in words:
            for w2 in words:
                if w1 == w2:
                    continue

                if w1 in w2:
                    res.append(w1)

        return list(set(res))