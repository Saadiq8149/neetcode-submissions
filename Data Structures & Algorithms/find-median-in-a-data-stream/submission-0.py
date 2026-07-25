class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify_max(self.max_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.max_heap,num)
        
        if self.min_heap and self.max_heap[0] > self.min_heap[0]:
            val = heapq.heappop_max(self.max_heap)
            heapq.heappush(self.min_heap, val)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, heapq.heappop_max(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush_max(self.max_heap, heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        diff = len(self.max_heap) - len(self.min_heap)

        if diff == 0:
            return (self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.max_heap[0]
        
        