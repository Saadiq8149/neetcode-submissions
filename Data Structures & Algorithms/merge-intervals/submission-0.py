class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals = sorted(intervals)

        for i in intervals:
            if not res:
                res.append(i)

            end = res[-1]
            
            if end[1] >= i[0]:
                res[-1] = [end[0], max(end[1], i[1])]
            else:
                res.append(i)

        return res