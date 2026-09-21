class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # searches dfs through each word with word_index 
        # as next item to look for, with letters already 
        #  need visit because only continue when word advances
        # and to avoid seeing the letter again
        def dfs(i, j, word_index, visit):
            print(i,j, visit)
            if word_index >= len(word):
                print("goat")
                return True
            if ((i,j) in visit or i < 0 or j < 0 or i >= len(board) or j >= len(board[0])):
                return False
            print(word[word_index], board[i][j], i, j)
            if (word[word_index] == board[i][j]):
                print("advance")
                visit.add((i,j))
                word_index+=1
                if dfs(i, j+1, word_index, visit) or \
                dfs(i+1, j, word_index,visit) or \
                dfs(i-1, j, word_index,visit) or \
                dfs(i, j-1, word_index,visit):
                    return True
            return False
            
# abce
# sfes
# adee
# ABCESEEEFS
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                # if c == first char in word:
                if board[i][j] == word[0]:
                    print("next")
                    if dfs(i,j,0, set()):
                        
                        return True
                    # search
        return False
                