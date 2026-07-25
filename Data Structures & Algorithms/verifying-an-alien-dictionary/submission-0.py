class Solution:
        def isAlienSorted(self, words: List[str], order: str) -> bool:
            mpp = {}
            for i, c in enumerate(order):
                mpp[c] = i

            for i in range(len(words) - 1):
                w1 = words[i]
                w2 = words[i + 1]

                j = 0
                while j < len(w1) and j < len(w2):
                    if w1[j] != w2[j]:
                        if mpp[w1[j]] > mpp[w2[j]]:
                            return False
                        break
                    j += 1
                else:
                    if len(w1) > len(w2):
                        return False

            return True