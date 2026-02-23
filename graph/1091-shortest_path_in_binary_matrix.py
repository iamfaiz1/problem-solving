from collections import deque
from typing import List
class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        q = deque()
        q.append((0, 0, 1))
        grid[0][0] = 1
        # visited = set((0, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]

        while q:
            i, j, count = q.popleft()
            if i==n-1 and j==n-1:
                return count
            for x, y in directions:
                nx, ny = i+x, j+y
                if 0<=nx <n and 0<=ny <n and grid[nx][ny] == 0:
                    q.append((nx, ny, count+1))
                    grid[nx][ny] = 1
        return -1
        


