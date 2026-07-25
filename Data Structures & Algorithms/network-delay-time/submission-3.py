class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n+1)]
        for s, d, w in times:
            adj[s].append((w, d))

        shortest = {}
        heap = [(0, k)]

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for w2, n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(heap, (w1+w2, n2))

        if len(shortest) != n:
            return -1

        res = float('-inf')
        for v in shortest.values():
            res = max(res, v)

        return res
