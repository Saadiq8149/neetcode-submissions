class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: [] for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    break

        topsort = []
        visit = set()
        cycle = set()

        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visit:
                return True

            visit.add(curr)
            cycle.add(curr)

            for nei in adj[curr]:
                if not dfs(nei):
                    return False

            cycle.remove(curr)
            topsort.append(curr)
            return True

        for n in adj:
            if not dfs(n):
                return ""
        topsort.reverse()
        return "".join(topsort)
                
