# memoization top down approach
class Solution:
    def knapsack(self, w, val, wt):
        # code here
        
        def sol(w, i):
            if memo[i][w] !=-1:
                return memo[i][w]
            
            if i==0:
                if wt[0] <=w:
                    memo[i][w] = val[0]
                else:
                    memo[i][w] = 0
                return memo[i][w]
                    
                
            if w < wt[i]:
                memo[i][w] = sol(w, i-1)
            else:
                memo[i][w] = max(sol(w, i-1), val[i] + sol(w-wt[i], i-1))
            return memo[i][w]
            
        n = len(val)
        memo = [[-1]*(w+1) for _ in range(n)]
        return sol(w, n-1)
            