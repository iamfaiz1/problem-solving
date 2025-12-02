# BFS queue implementation
from collections import defaultdict, deque
class Solution:
    def isCycle(self, V, edges):
        graph = defaultdict(list)
        
        # Build undirected graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        for start in range(V):
            if start not in visited:
                q = deque([(start, -1)])  # (node, parent)
                visited.add(start)
                
                while q:
                    node, parent = q.popleft()

                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append((neighbor, node))
                        elif neighbor != parent:
                            # Found a back edge -> cycle
                            return True
        return False

# ----------------------------------------------------------------------
# DFS stack implementation

class Solution:
    def isCycle(self, v, edges):
        #Code here
        from collections import defaultdict
        graph = [[] for _ in range(v)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False]*v
        
        for n in range(v):
            if not visited[n]:
                visited[n] = True
                stack = [(n, -1)]       #(node, parent)
                while stack:
                    node, parent = stack.pop()
                    for nodes in graph[node]:
                        if not visited[nodes]:
                            visited[nodes] = True
                            stack.append((nodes, node))
                        elif parent != nodes:
                            return True
        return False
            
		
		