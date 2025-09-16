from collections import Counter
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        length, width = len(board), len(board[0])
        # FOLLOW ups optimizaTION:

        # word is large then board size

        # currently wasnt useful and it increased few milli sec of runtime
        # if len(word) > length*width:
        #     return False
        
        # word character are more than board
        wc = Counter(word)
        bc = Counter( ch for row in board for ch in row)
        for b in bc:
            if wc[b]>bc[b]:
                return False
        
        # if end has less common characters then start from end
        if bc[word[0]] > bc[word[-1]]:
            word = word[::-1]


        def backtrack(row, col, idx):
            # base condition
            if idx == len(word):
                # we are considering only matchnig characters
                return True

            # checking for valid move
            if (row < 0 or row >= length or 
                col < 0 or col >= width or 
                board[row][col] != word[idx]):
                return False

            # to avoid rechecking
            temp = board[row][col]
            board[row][col] = "_"

            res = ( backtrack(row+1, col, idx+1) or   #down
                    backtrack(row-1, col, idx+1) or   #up
                    backtrack(row, col+1, idx+1) or   #rirght
                    backtrack(row, col-1, idx+1) )    #left
            
            # backtrack restored
            board[row][col] = temp
            return res
        
        for i in range(length):
            for j in range(width):
                if backtrack(i, j, 0):
                    return True
        return False
