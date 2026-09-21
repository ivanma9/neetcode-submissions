class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # i 
        def isPali(word):
            l,r = 0, len(word) -1
            while(l < r):
                if word[l] != word[r]:
                    return False
                l+=1
                r-=1
            return True

        # a ab
        res = []
        def dfs(cur, i):

            if i == len(s):
                res.append(cur.copy())
                return
            
            # cur.append(s[:i])

            #partition

            for j in range(i, len(s)):
                # if word from i to j is pali
                print(i,j, s[i:j+1])
                if isPali(s[i:j+1]):
                    
                    cur.append(s[i:j+1]) #a ,# aa # aab
                    dfs(cur, j+1)
                    cur.pop()
        dfs([],0)

        return res



        

