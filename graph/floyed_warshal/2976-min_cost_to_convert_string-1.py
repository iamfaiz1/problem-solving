class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        inf = float('inf')
        graph = [[inf]*26 for _ in range(26)]
        for i in range(26):
            graph[i][i] = 0
        
        # initialization
        for i in range(len(original)):
            u = ord(original[i])-ord('a')
            v = ord(changed[i])-ord('a')
            graph[u][v] = min(graph[u][v], cost[i])

        
        # floyed warshal
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
        
        # finding total cost
        totalcost = 0
        for i in range(len(source)):
            s = ord(source[i]) - ord('a')
            t = ord(target[i]) - ord('a')
            
            if graph[s][t] == inf:
                return -1
            totalcost += graph[s][t]
        return totalcost
        
        
        
        