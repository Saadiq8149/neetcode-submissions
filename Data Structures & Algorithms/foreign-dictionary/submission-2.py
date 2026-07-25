class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        topSort = []
        visit = set()
        path = set()

        for char in adj:
            if not self.dfs(char, adj, visit, path, topSort):
                return ""

        topSort.reverse()
        return "".join(topSort)

    def dfs(self, src, adj, visit, path, topSort):
        if src in path:
            return False 

        if src in visit:
            return True

        path.add(src)

        for nei in adj[src]:
            if not self.dfs(nei, adj, visit, path, topSort):
                return False

        path.remove(src)
        visit.add(src)
        topSort.append(src)

        return True