class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid)<3 or len(grid[0]) <3:
            return 0

        count = 0
        m = len(grid)
        n = len(grid[0])

        def check(i, j):
            # pruning:
                # if 3x3 matrix each has to be equal sum them center must be 5
            if grid[i+1][j+1] !=5:
                return False

            # # checking if 9 elements consist of 1-9
            # exactly once
            seen = set()
            for x in range(3):
                for y in range(3):
                    val = grid[i + x][j + y]
                    if val < 1 or val > 9 or val in seen:
                        return False
                    seen.add(val)
            
            ### logic
                # sum(1...9) = 45
                # no. of rows = 3
                # each row has 45/3 = 15

            # testing for row: 
            for r in range(3):
                if sum(grid[i + r][j + c] for c in range(3)) != 15:
                    return False
            # testing for col: 
            for c in range(3):
                if sum(grid[i + r][j + c] for r in range(3)) != 15:
                    return False
            
            # check diagonals
            if sum(grid[i + d][j + d] for d in range(3)) != 15:
                return False
            if sum(grid[i + d][j + 2 - d] for d in range(3)) != 15:
                return False

            return True

        # for each grid
        for i in range(m-2):
            for j in range(n-2):
                # call funtion
                if check(i, j):
                    count+=1
        
        return count

        
            
        