class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                left = dp[i-1][j] 
                top = dp[i][j-1] 
                dp[i][j] = top + left
        return dp[m-1][n-1]