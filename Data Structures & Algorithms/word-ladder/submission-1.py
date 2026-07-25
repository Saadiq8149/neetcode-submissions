class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
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