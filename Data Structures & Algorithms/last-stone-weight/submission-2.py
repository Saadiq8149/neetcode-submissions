class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:        
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            print(stones)
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            print(x, y)

            if x != y:
                heapq.heappush_max(stones, abs(y - x))


        return 0 if len(stones) == 0 else stones[0]

        

