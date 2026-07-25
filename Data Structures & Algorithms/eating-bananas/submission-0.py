class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        result = high

        while low <= high:
            k = (low + high) // 2
            
            time = 0
            for p in piles:
                time += math.ceil(float(p)/k)

            if time <= h:
                result = k
                high = k - 1
            else:
                low = k + 1
        return result