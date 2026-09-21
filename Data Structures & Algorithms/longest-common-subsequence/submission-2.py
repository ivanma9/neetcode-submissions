class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     s c a t
    # b.  0 0 0 0
    # c.  0 1 0 0
    # r.  0 0 1 1
    # a   0 0 2 2
    # s.  0 0 
    # t.  0 0

    # init all to 0
    # dp = of [0] * n+1 and m+1

        ROWS = len(text1)
        COLS = len(text2)
        dp = [[0] * (COLS+1) for _ in range(ROWS+1)]
        maxCount = 0
        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                top = dp[i-1][j]
                left = dp[i][j-1]
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(top,left)
                    # maxCount = max(maxCount, dp[i][j])
        print(dp)

        return dp[ROWS][COLS]

# 0.   j  m  j  k  b  k  j. k  v
# 0[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
# b[0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
# s[0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
# b[0, 0, 0, 0, 0, 2, 2, 2, 2, 2], 
# i[0, 0, 0, 0, 0, 2, 2, 2, 2, 2], 
# n[0, 0, 0, 0, 0, 2, 2, 2, 2, 2], 
# i[0, 0, 0, 0, 0, 2, 2, 2, 2, 2], 
# n[0, 0, 0, 0, 0, 2, 2, 2, 2, 2], 
# m[0, 0, 1, 1, 1, 2, 2, 2, 2, 2]]



