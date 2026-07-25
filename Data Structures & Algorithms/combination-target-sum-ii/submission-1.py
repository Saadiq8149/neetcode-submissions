class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def recurse(i=0, curr=[]):
            s = sum(curr)
            if i >= len(candidates) or s >= target:
                if s == target:
                    res.append(curr[:])
                return

            curr.append(candidates[i])
            recurse(i+1, curr)
            curr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            recurse(i+1, curr)

        recurse()
        return res
