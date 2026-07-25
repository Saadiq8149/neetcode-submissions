class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [count[k] for k in count]
        heapq.heapify_max(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            
            if not maxHeap:
                time = q[0][1]
            else:
                count = heapq.heappop_max(maxHeap) - 1
                if count:
                    q.append((count, time + n))

            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])

        return time
