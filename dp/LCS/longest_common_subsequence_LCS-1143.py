class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        memo = dict()

        def solve(i, j):
            if i<0 or j<0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if t1[i]==t2[j]:
                memo[(i, j)] = solve(i-1, j-1) +1
            else:
                memo[(i, j)] = max(solve(i-1, j), solve(i, j-1))
            return memo[(i, j)]
            
        return solve(len(t1)-1, len(t2)-1)
    
# --------------------------------------------------------------
# using lru_cache : inbuild memoization

class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:

        @lru_cache(None)
        def solve(i, j):
            if i<0 or j<0:
                return 0

            if t1[i]==t2[j]:
                return solve(i-1, j-1) +1
            else:
                return max(solve(i-1, j), solve(i, j-1))
            
        
        return solve(len(t1)-1, len(t2)-1)
# --------------------------------------------------------------
# bottom-up approach: tabulation method

class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        n1 = len(t1)+1
        n2 = len(t2)+1

        dp = [[0]*n2 for _ in range(n1)]

        for i in range(1, n1):
            for j in range(1, n2):
                if t1[i-1] == t2[j-1]:
                    dp[i][j]=  dp[i-1][j-1] +1
                else:
                    dp[i][j]=  max(dp[i-1][j], dp[i][j-1])

        return dp[len(t1)][len(t2)]