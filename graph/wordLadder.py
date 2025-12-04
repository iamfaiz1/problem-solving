class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # buidling pattern-graph
        from collections import defaultdict, deque
        graph = defaultdict(list)
        blength = len(beginWord)

        for word in wordList:
            for i in range(blength):
                pattern = word[:i]+'*'+ word[i+1:]
                graph[pattern].append(word)
        
        q = deque([(beginWord, 1)])
        visited = set(beginWord)

        # applying BFS- to get min steps
        while q:
            # print(q)
            word, lvl = q.popleft()

            for i in range(blength):
                pattern = word[:i]+ '*'+ word[i+1:]
                for neighbour in graph[pattern]:
                    if neighbour == endWord:
                        return lvl +1
                    
                    elif neighbour not in visited:
                        q.append((neighbour, lvl+1))
                        visited.add(neighbour)
                
        return 0



