class Solution:
    def oneCharDiff(self, w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
        return True if diff <= 1 else False
        

    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        adj = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                w1 = wordList[i]
                w2 = wordList[j]
                if self.oneCharDiff(w1, w2):
                    adj[w1].append(w2)
                    adj[w2].append(w1)

        for w in wordList:
            if self.oneCharDiff(beginWord, w):
                adj[w].append(beginWord)
                adj[beginWord].append(w)

        q = deque()
        q.append(beginWord)

        visited = set()
        ops = 1
        while q:
            n = len(q)
            for _ in range(n):
                w = q.popleft()
                if w == endWord:
                    return ops
                visited.add(w)
                for n in adj[w]:
                    if n in visited:
                        continue
                    q.append(n)

            ops += 1
        return 0

                


