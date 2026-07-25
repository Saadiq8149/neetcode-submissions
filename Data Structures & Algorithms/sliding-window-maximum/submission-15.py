class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i in range(k):
            heapq.heappush_max(heap, (nums[i], i))
        
        res = []
        for r in range(k, len(nums)):
            l = r - k
            res.append(heap[0][0])
            heapq.heappush_max(heap, (nums[r], r))
            while heap[0][1] <= l:
                heapq.heappop_max(heap)
        res.append(heap[0][0])

        return res
        



        