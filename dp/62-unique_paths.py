class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        di = (
            (0, 1),
            (1, 0)
        )
        memo = {}

        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                if i==m-1 and j==n-1:
                    return 1
                
                memo[(i, j)] = 0
                for x, y in di:
                    nx = x + i
                    ny = y + j
                    if 0 <= nx < m and 0 <= ny < n:
                        memo[(i, j)] += solve(nx, ny)
                return memo[(i, j)]
        return solve(0, 0)

# ---------------------------------------------------------------------

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        di = (
            (0, 1),
            (1, 0)
        )

        dp[m-1][n-1]=1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                for x, y in di:
                    nx = x + i
                    ny = y + j
                    if 0 <= nx < m and 0 <= ny < n:
                        dp[i][j] += dp[nx][ny]
        return dp[0][0]                



