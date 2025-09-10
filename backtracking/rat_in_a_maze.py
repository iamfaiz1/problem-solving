class Solution:
    # Function to find all possible paths
    def ratInMaze(self, maze):
        # code here
        res =[]
        n = len(maze)
        visited = [[False]*n for _ in range(n)]
        
        # checking for valid move
        # order for checking must be:
        # down, left, right, up
        
        # di = [d,l,r,u]
        di = [(1, 0, 'D'),(0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]
        
        def is_valid(row, col, visited):
            return (0<=row<n and 0<=col<n and maze[row][col]== 1 and not visited[row][col])
        
        
        # main maze function
        def backtrack(row, col, move):
            if row == n-1 and col == n-1:
                res.append(move[:])
                return 
            
            visited[row][col] = True
              
            for r, c, m in di:
                new_row, new_col = row+r, col+c
                
                if is_valid(new_row, new_col, visited):
                    backtrack(new_row, new_col, move+m)
                
            visited[row][col] = False
       
        if maze[0][0]==1:     
            backtrack(0, 0, "")
        return res
                
                
                
                
        