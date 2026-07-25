class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []

        for i in intervals:
            if newInterval:
                if i[0] > newInterval[1]:        
                    res.append(newInterval)
                    res.append(i)
                    newInterval = None
                elif i[1] >= newInterval[0]:       
                    newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
                else:                             
                    res.append(i)
            else:
                res.append(i)

        if newInterval:                            
            res.append(newInterval)

        return res