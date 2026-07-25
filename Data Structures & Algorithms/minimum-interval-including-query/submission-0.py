class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        res = []

        for q in queries:
            minLength = -1
            for start, end in intervals:
                length = end - start + 1
                if start <= q and q <= end:
                    if minLength == -1:
                        minLength = length
                    else:
                        minLength = min(minLength, length)

            res.append(minLength)

        return res
        
