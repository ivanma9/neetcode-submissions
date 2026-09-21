class Solution:


    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,j, word_i):
            if  i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == "1":
                return False
            if word[word_i] != board[i][j]:
                return False
            else:
                #now we branch to its 4 neighbors
                #inc word_i
                temp = board[i][j]
                board[i][j] = "1" #using char
                word_i += 1
                if word_i == len(word):
                    #word is finished
                    board[i][j] = temp
                    return True

                res = dfs(i+1,j,word_i) or dfs(i-1,j,word_i) or dfs(i,j+1,word_i) or dfs(i,j-1,word_i)
                board[i][j] = temp # changes back to char 
                return res

        #dfs
        #track visiting with "1" as a used or visited
        # we can not use and revisit
        for r in range(len(board)):
            for c in range(len(board[0])):
                # iterate word from beginning
                if word[0] == board[r][c]:
                    if dfs(r,c, 0):
                        return True
        return False


