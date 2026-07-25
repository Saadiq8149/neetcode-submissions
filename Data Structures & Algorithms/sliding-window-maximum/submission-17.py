class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        
        res = []
        for r in range(k, len(nums)):
            l = r - k
            res.append(-heap[0][0])
            heapq.heappush(heap, (-nums[r], r))
            while heap[0][1] <= l:
                heapq.heappop(heap)
        res.append(-heap[0][0])

        return res
        



        