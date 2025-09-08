# brute force + backtracking
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        arr = [["."] * n for _ in range(n)]

        def is_safe( row, col):
            # check in column:
            for i in range(n):
                # check in same column
                if arr[i][col]=='Q' and i!=row:
                    return False

                # if:__
                # checking in same row is not needed
                # as we are placing only one queen in each row 
                # (we never placed 2 queen in same row)

            # check upper left digonal
            i = row-1
            j = col-1
            while i>=0 and j>=0:
                if arr[i][j] == 'Q':
                    return False
                i-=1
                j-=1

            # check upper right dig
            i = row-1
            j = col+1
            while i>=0 and j<n:
                if arr[i][j] == 'Q':
                    return False
                i-=1
                j+=1
            return True

        def n_queens( row):
            # base case
            if row == n:
                ans.append( ["".join(arr[k]) for k in range(n)] )
                print(ans)
                return

            for col in range(n):
                # calling is_safe 
                if is_safe(row, col):
                    arr[row][col]="Q"

                    # recursive self-call
                    n_queens( row +1)

                    # backtrack
                    arr[row][col]='.'
        n_queens(0)
        return ans
                    
# ______________________________________________________________________________________
# optimized approach using set and backtracking

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        arr = [["."] * n for _ in range(n)] 
        column = set()
        dig_ul = set()
        dig_ur = set()


        def n_queens( row):
            # base case
            if row == n:
                ans.append( ["".join(arr[k]) for k in range(n)] )
                return

            for col in range(n):
                if col in column or (row-col) in dig_ul or (row+col) in dig_ur:
                    continue #no need to use
                
                arr[row][col]="Q"
                column.add(col)
                dig_ul.add(row- col)
                dig_ur.add(row +col)

                # recursive self-call
                n_queens( row +1)

                # backtrack
                arr[row][col]='.'
                column.remove(col)
                dig_ul.remove(row- col)
                dig_ur.remove(row +col)

        n_queens(0)
        return ans
                    