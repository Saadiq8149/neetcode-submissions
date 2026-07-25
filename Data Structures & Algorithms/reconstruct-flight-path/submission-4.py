class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for s, d in tickets:
            adj[s].append(d)

        for k in adj:
            adj[k].sort()
        
        res = ["JFK"]
        def dfs(curr):
            if len(res) == len(tickets) + 1:
                return True

            if curr not in adj:
                return False

            temp = list(adj[curr])
            for i, v in enumerate(temp):
                adj[curr].pop(i)
                res.append(v)
                if dfs(v):
                    return True 

                adj[curr].insert(i, v)
                res.pop()
            return False
        dfs("JFK")
        return res
        