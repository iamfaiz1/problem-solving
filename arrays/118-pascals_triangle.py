class Solution:
    def generate(self, n: int) -> list[list[int]]:
        ans = []
        for i in range(n):
            row = [1] * (i + 1)
            
            for j in range(1, i):
                row[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(row)
        return ans

# ----------------------------------------------------------------------------------
# --                 bruteforece: doule loop (passed) fz special                  --

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        
        arr = [1, 1]
        if n==2:
            return [[1], arr]
        
        ans = []
        for i in range(n):
            li = [0]*(i+1)
            ln = len(li)
            for j in range(ln):
                if j==0 or j==ln-1:
                    li[j] = 1
                else:
                    li[j] = arr[j-1] +arr[j]
            arr = li[:]
            ans.append(li)
        return ans
                    