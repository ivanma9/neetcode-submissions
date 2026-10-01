class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        m =len(word1)
        n = len(word2)

        memo = {}
        
        def traverse(i,j):
            # go through character by character either 
            if i == m:
                # end of w1
                # remove from w2 (n-j)
                return n - j 
            if j == n:
                # end of w1
                # remove from w2 (n-j)
                return m - i
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i] == word2[j]:
                ans = traverse(i+1,j+1)
            else:
                # replace
                rep = 1 + traverse(i+1,j+1)
                # add
                add = 1 + traverse(i+1,j)
                # remove
                rem = 1 + traverse(i,j+1)
                ans = min(rep,add,rem)
            memo[(i,j)] = ans
            
            return ans
        return traverse(0,0)