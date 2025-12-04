class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # for dfs lookup
        def dfs(i, j):
            nonlocal flag
            # no need to pop root node
            if (i==m-1 or i==0 or j==0 or j==n-1):
                flag = True
                return
            
            # visited.add((i, j))
            grid[i][j]=2

            for x, y in di:
                ni, nj = x+i, y+j

                if 0<=ni <m and 0<=nj <n and grid[ni][nj] == 0:
                    dfs(ni, nj)

# ---------------------------------------------
# main function
        m, n = len(grid), len(grid[0])
        # visited = set()

        di = [
            # directions to check
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        count = 0
        # skipiing boundry index for optimization
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j]==0 :
                    # no need to push root node
                    flag = False
                    dfs(i, j)
                    if not flag:
                        count+=1
                        flag = False
        return count
        


            
                
        
