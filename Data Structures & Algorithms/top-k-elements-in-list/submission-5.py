class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        
        freq = Counter(nums)
        for key,v in freq.items():
            heapq.heappush_max(heap, (v, key))

        return [heapq.heappop_max(heap)[1] for _ in range(k)]
