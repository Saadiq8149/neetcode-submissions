class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            return math.sqrt(p[0]**2 + p[1]**2)

        points.sort(key=dist)

        return points[:k]

        
