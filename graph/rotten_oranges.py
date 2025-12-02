class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()

        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j, 0))
        directions = [
            (1, 0),     #down
            (-1, 0),    #up
            (0, 1),     #right
            (0, -1),    #left
        ]
        maxtime = 0
        while(q):
            i, j, time = q.popleft()
            maxtime = max(time, maxtime)

            for di, dj in directions:
                ni, nj = di+i, dj+j
                if 0 <= ni < n and 0 <=nj <m and grid[ni][nj]==1:
                    grid[ni][nj]=2
                    q.append((ni, nj, time+1))
        
        # check for good orange:
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return maxtime

# -------------------------------------------------
"""
at the end we scanned the grid again to check if any good orange is left...
but, we could have maintained a count of good oranges while inserting rotten oranges in the queue initially
and decremented that count whenever we rot a good orange.

this will imrove the time complexity slightly.
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()

        n = len(grid)
        m = len(grid[0])
        good_oranges = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j, 0))
                elif grid[i][j]==1:
                    good_oranges += 1
        directions = [
            (1, 0),     #down
            (-1, 0),    #up
            (0, 1),     #right
            (0, -1),    #left
        ]
        maxtime = 0
        while(q):
            i, j, time = q.popleft()
            maxtime = max(time, maxtime)

            for di, dj in directions:
                ni, nj = di+i, dj+j
                if 0 <= ni < n and 0 <=nj <m and grid[ni][nj]==1:
                    grid[ni][nj]=2
                    good_oranges -= 1
                    q.append((ni, nj, time+1))
        
        # check for good orange:
        if good_oranges > 0:
            return -1
        return maxtime

# ----------------------------------------------------------------------
# using additional for loop and size variable for faster iteration
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        q = deque()

        n = len(grid)
        m = len(grid[0])
        good_oranges = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j, 0))
                elif grid[i][j]==1:
                    good_oranges += 1

        directions = [
            (1, 0),     #down
            (-1, 0),    #up
            (0, 1),     #right
            (0, -1),    #left
        ]
        maxtime = 0
        while(q):
            # using size and for loop for faster iteration,
            # as we know for is faster than while loop
            size = len(q)
            for _ in range(size):
                i, j, time = q.popleft()
                maxtime = max(time, maxtime)

                for di, dj in directions:
                    ni, nj = di+i, dj+j
                    if 0 <= ni < n and 0 <=nj <m and grid[ni][nj]==1:
                        grid[ni][nj]=2
                        good_oranges -= 1
                        q.append((ni, nj, time+1))
        
        # check for good orange:
        if good_oranges > 0:
            return -1
        return maxtime

