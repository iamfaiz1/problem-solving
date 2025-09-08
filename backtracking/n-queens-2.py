
# have to return the count of distinct solutions
# O(n!) time and O(n) space

class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        column = set()
        dig_ul = set()
        dig_ur = set()


        def queens(row):
            nonlocal count
            if row == n:
                count += 1
                return
            
            for col in range(n):
                if col in column or row-col in dig_ul or row+col in dig_ur:
                    continue
                # recursive call
                column.add(col)
                dig_ul.add(row-col)
                dig_ur.add(row+col)

                queens(row +1)

                # backtrack
                column.remove(col)
                dig_ul.remove(row-col)
                dig_ur.remove(row+col)

        queens(0)
        return count