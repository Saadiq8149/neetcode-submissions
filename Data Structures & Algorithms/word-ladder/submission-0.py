class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = {}

        for w1 in wordList:
            graph[w1] = []
            for w2 in wordList:
                if w1 != w2:
                    diff = 0
                    for i in range(len(w1)):
                        if w1[i] != w2[i]:
                            diff += 1
                    if diff == 1:
                        graph[w1].append(w2)

        graph[beginWord] = []

        for w in wordList:
            diff = 0
            for i in range(len(w)):
                if w[i] != beginWord[i]:
                    diff += 1
            if diff == 1:
                graph[beginWord].append(w)

        q = deque([(beginWord, 1)]) 
        visited = set([beginWord])

        while q:
            node, steps = q.popleft()
            
            if node == endWord:
                return steps

            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    q.append((n, steps + 1))

        return 0