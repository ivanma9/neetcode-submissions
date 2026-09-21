class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # i = 0

        # while (i < len(s)):

        #     for word in wordDict:
        #         j = 0
        #         prev_i =i
        #         while (j < len(word) and i < len(s) 
        #             and s[i] == word[j]):
        #             i+=1
        #             j+=1
        #         # went through s
        #         if i == len(s):
        #             return True
        #         # if i did not go through all of word
        #         # bring back to prev_i
        #         if j < len(word):
        #             i = prev_i
        # return False
        word_dict = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        # i starting pos
        i = n
        for i in range(n-1, -1,-1):
            for w in wordDict:
                if (i+ len(w) <= n and
                    s[i: i+len(w)] == w):
                    #found
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
            
        return dp[0]
            
            
            

        # while(i < len(s) and j < len(s)):
        #     if s[i:j] in word_dict:
        #         # word found move up i
        #         i = j + 1

        #     else:
        #         # word not found lets extend the possibilities
        #         j+=1


                

        



                

