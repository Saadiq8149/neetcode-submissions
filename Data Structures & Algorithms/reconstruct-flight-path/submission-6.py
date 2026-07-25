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

            for i, n in enumerate(adj[curr]):
                if n == "":
                    continue
                adj[curr][i] = ""
                res.append(n)
                if dfs(n):
                    return True
                adj[curr][i] = n
                res.pop()
            return False

        dfs("JFK")
        return res
        