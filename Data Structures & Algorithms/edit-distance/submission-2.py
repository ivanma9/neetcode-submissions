class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # add, replace, delete

        # if match: no op

        # if character -> replace

        # if character in 1, not in 2-> delete
        # if character in 2, not in 1-> add

        # subproblem is [i:]

        # try all possibilitiyes
        m = len(word1)
        n= len(word2)
        memo = {}
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            if i == m and j < n:
                # remove remaining n-j
                return n-j
            if j == n and i < m:
                # add remoaining m- i
                return m-i
            if j==n and i == m:
                # end
                return 0
            
            #recursive
            if word1[i] == word2[j]:
                ans = dfs(i+1,j+1)
                memo[(i,j)] = ans

                return ans
            #add replace or remove
            ans =1 + min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))
            memo[(i,j)] = ans
            return ans


        return dfs(0,0)
            


                