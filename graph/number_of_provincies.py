class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # creating adjency list first
        from collections import defaultdict
        graph = defaultdict(list)
        n = len(isConnected)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    graph[i].append(j)
        
        # applying dfs:
        count = 0        
        visited = [False]*n

        for g in range(n):
            if not visited[g]:
                count+=1
                stack = [g]
                visited[g]=True

                while(stack):
                    node = stack.pop()
                    visited[node]=True
                    for i in graph[node]:
                        if not visited[i]:
                            stack.append(i)
        return count

                

# -------------------------------------------------------------------------
# adjency matrix approach
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        def dfs(i):
            for j in range(n):
                if isConnected[i][j]==1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited:
                count+=1
                visited.add(i)
                dfs(i)
        return count
    
# --------------------------------------------------------------------------
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        def dfs(i):
            while stack:
                node = stack.pop()
                for j in range(n):
                    if isConnected[node][j]==1 and j not in visited:
                        visited.add(j)
                        stack.append(j)
        
        visited = set()
        count = 0
        stack = []
        for i in range(n):
            if i not in visited:
                count+=1
                stack.append(i)
                visited.add(i)
                dfs(i)
        return count
    