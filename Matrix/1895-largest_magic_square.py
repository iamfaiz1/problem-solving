class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def check(x, y, k):
            target = sum(grid[x][y:y+k])

            # rows
            for i in range(x, x+k):
                if sum(grid[i][y:y+k]) != target:
                    return False

            # cols
            for j in range(y, y+k):
                if sum(grid[i][j] for i in range(x, x+k)) != target:
                    return False

            # main diagonal
            if sum(grid[x+i][y+i] for i in range(k)) != target:
                return False

            # anti diagonal
            if sum(grid[x+i][y+k-1-i] for i in range(k)) != target:
                return False

            return True

        # every single cell is a magic square
        ans = 1

        k = min(m, n)
        while k >0:
            for i in range(m -k + 1):
                for j in range(n - k + 1):
                    if check(i, j, k):
                        return k
            k-=1
        return ans


# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------




# slower approach
class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        def check(x, y, k):
            # row check
            row = 0
            flag = True
            for i in range(k):
                temp = 0
                for j in range(k):
                    temp += grid[i+x][j+y]
                if flag:
                    flag = False
                    row = temp
                elif row != temp:
                    return False
            
            # col check
            col = 0
            flag = True
            for i in range(k):
                temp = 0
                for j in range(k):
                    temp += grid[j+x][i+y]
                if flag:
                    flag = False
                    col = temp
                elif col != temp:
                    return False
            # row and col:
            if row != col:
                return False
            
            # dig check
            dig1 = 0
            dig2 = 0
            for i in range(k):
                dig1 += grid[i+x][i+y]
                dig2 += grid[i+x][y+k-1-i]
            
            # dig check
            if dig1 !=dig2:
                return False
            
            # row col dig
            if row != dig1:
                return False

            # final return
            return True

        # edge case
        if len(grid)==1 or len(grid[0])==1:
            return 1

        ma = 1
        k = min(len(grid), len(grid[0]))

        while(k >0):
            for i in range(len(grid)-k+1):
                for j in range(len(grid[0])-k+1):
                    if check(i, j, k):
                        return k
            k-=1

        return ma