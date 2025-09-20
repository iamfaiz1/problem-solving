class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # collecting to know what to solve for
        empty = [(i, j) for i in range(9) for j in range(9) if board[i][j]=="."]

        def is_valid(r, c, d):
            # col check
            for i in range(9):
                if board[i][c] == d:
                    return False
            # row check
            for j in range(9):
                if board[r][j] == d:
                    return False
            
            # sub board check
            row =( r//3) *3
            col =( c//3) *3
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if board[i][j] == d:
                        return False
            # finally
            return True
        
        
        def backtrack(k):
            if k==len(empty):
                return True
            
            r, c = empty[k]
            
            for d in map(str, range(1, 10)):
                if is_valid(r, c, d):
                    board[r][c]= d
                    if backtrack(k+1):
                        return True
                    board[r][c] = "."
            return False
        
        backtrack(0)
        # return wasnt requried


# ___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# optimised lookup for validity check
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # collecting to know what to solve for
        empty = [(i, j) for i in range(9) for j in range(9) if board[i][j]=="."]

        # row_track = [set(), set(),...9]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # initializing sets
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    d = board[i][j]
                    rows[i].add(d)
                    cols[j].add(d)
                    boxes[(i // 3) * 3 + (j // 3)].add(d)
        
        
        def backtrack(k):
            if k==len(empty):
                return True
            
            r , c = empty[k]
            b = (r//3)*3 + (c//3)

            
            for d in map(str, range(1, 10)):
                if (d not in rows[r] 
                    and d not in cols[c] 
                    and d not in boxes[b]):

                    # add
                    board[r][c] = d

                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)

                    if backtrack(k+1):
                        return True

                    # backtrrack
                    board[r][c] = "."
                    
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[b].remove(d)
                    
            return False
        
        backtrack(0)

# ______________________________________________________________________________
