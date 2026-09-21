class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == "" and s2 == "" and s3 == "":
            return True
        m = len(s1)
        n = len(s2)
        if (m+n != len(s3)):
            return False
        dp=[[False] * (n+1) for i in range(m+1)]
        dp[m][n] = True
        # check if either 
        for i in range(m, -1, -1):
            for j in range(n,-1,-1):
                if (i < m and s1[i]== s3[i+j] and dp[i+1][j]):
                    dp[i][j] = True
                if (j < n and s2[j]== s3[i+j] and dp[i][j+1]):
                    dp[i][j] = True
        return dp[0][0]
# s1="aa"
# s2="ab"
# s3="abaa"
#   012
#   ab_j
# 0a
# 1a  F
# 2_TTT  
# i

