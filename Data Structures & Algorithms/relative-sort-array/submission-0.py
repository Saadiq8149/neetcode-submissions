class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        res = []
        for n in arr2:
            while freq[n]:
                res.append(n)
                freq[n] -= 1

        for k, v in sorted(freq.items()):
            while freq[k]:
                res.append(k)
                freq[k] -= 1

        return res