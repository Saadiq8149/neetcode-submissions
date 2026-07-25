class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        i, j, k = -1, -1, -1
        
        for t in range(len(triplets)):
            a, b, c = triplets[t]

            if a > target[0] or b > target[1] or c > target[2]:
                continue
            
            if a == target[0]:
                i = t
            if b == target[1]:
                j = t
            if c == target[2]:
                k = t

        return i != -1 and j != -1 and k != -1