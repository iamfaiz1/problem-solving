from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])

        di = [
            (-1, 0),
            (0, -1),
            (0, 1),
            (1, 0)
        ]
        def bfs(i, j):
            grid[i][j]= -1
            q.append((i, j, 0))
            while q:
                x, y, _ = q.popleft()
                for i, j in di:
                    nx, ny = x+i, y+j
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                        q.append((nx, ny, 0))
                        grid[nx][ny]=-1
        
        flag = False
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    # call bfs 1
                    bfs(i, j)
                    flag = True
                    break
            if flag:
                break

        ans =  0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==-1:
                    q.append((i, j, 0))

        while q:
            x, y, d = q.popleft()
            ans = max(ans, d)
            for i, j in di:
                ni, nj = x+i, y+j
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]==0:
                    q.append((ni, nj, d+1))
                    grid[ni][nj]=-1
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]==1:
                    return d
        return ans