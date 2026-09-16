# -------------------------------------------------------------
# DFS approach
# -------------------------------------------------------------
from collections import defaultdict
class Solution1:
    def canFinish(self, n: int, prerequisites: list[list[int]]) -> bool:
        # converting to graph form
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[p].append(c)
        # print(graph)

        vis = [False]*n
        path = [False]*n

        def dfs(p):
            if path[p]:
                return False
            
            if vis[p]:
                return True
                # because if it was false we would have returned immediatly and couldnt get a duplicate prerequisite
            vis[p] = True
            path[p] = True

            for c in graph[p]:
                # print(p, c)
                if not dfs(c):
                    return False
            path[p] = False
            return True

        # checking all courses
        for i in range(n):
            if not dfs(i):
                return False

        return True



# -------------------------------------------------------------
# Topological sort approach
# -------------------------------------------------------------

from collections import defaultdict, deque
class Solution:
    def canFinish(self, n: int, prerequisites: list[list[int]]) -> bool:
        # converting to graph form
        indegree = [0]*n
        graph = defaultdict(list)
        for c, p in prerequisites:
            graph[p].append(c)
            indegree[c] +=1
            # print(indegree)


        count = 0
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            p = q.popleft()
            count +=1
            for c in graph[p]:
                # print(p, c)
                indegree[c] -=1

                if indegree[c]==0:
                    q.append(c)

        return count==n

        