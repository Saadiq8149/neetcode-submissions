class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)

        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)

            if x == y:
                continue
            else:
                heapq.heappush_max(stones, abs(y - x))
        
        return 0 if not stones else stones[0]