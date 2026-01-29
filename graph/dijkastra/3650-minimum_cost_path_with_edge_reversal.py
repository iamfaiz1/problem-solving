from collections import defaultdict
import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # converting to adjency list and adding reversed edges
        adj_graph = defaultdict(list)
        for u, v, w in edges:
            adj_graph[u].append((v, w))
            adj_graph[v].append((u, w*2))
        
        # applying dijkastra to find cheapest path between 0 and n-1th node

        def dijkastra(adj_graph, n, source):
            distance = [float('inf') for i in range(n)]
            distance[source] = 0

            priorityQ = [(0, source)]

            while priorityQ:
                d, u = heapq.heappop(priorityQ)
                if d > distance[u]:
                    continue
                
                for v, w in adj_graph[u]:
                    if d+w < distance[v]:
                        distance[v] = d+w
                        heapq.heappush(priorityQ, (distance[v], v))    
            if distance[-1] == float('inf'):
                return -1
            # returning minimum cost to reach n-1th node from 0th node
            # distance array contains minimum cost to reach each node from source
            return distance[-1]
        return dijkastra(adj_graph, n, 0)


        
        


        
