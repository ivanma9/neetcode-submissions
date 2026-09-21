
class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def add(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.isWord = True
        

    # def search(self, word):
    #     node = self
    #     for c in word:
    #         if c is not in node.children:
    #             node.children[c] = Trie()
    #         node = node.children[c]
    #     node.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = Trie()

        for word in words:
            t.add(word)
        # make prefix tree
        # print(t.children['b'].children['a'].children['c'].children['k'].children['e'].children['n'].children['d'].children)

        res = set()
        visit = set()

        def dfs(i,j,node, word):
            if i < 0 or j < 0 or i >= len(board) or j  >= len(board[0]) \
            or (i,j) in visit or board[i][j] not in node.children:
                return
            print(i,j , board[i][j])
            visit.add((i,j))
            node = node.children[board[i][j]]
            word += board[i][j]

            if node.isWord:
                print("word")
                res.add(word)
            
            dfs(i+1,j,node, word)
            dfs(i-1,j,node, word)
            dfs(i,j+1,node, word)
            dfs(i,j-1,node, word)
            visit.remove((i,j))




        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j, t, "")

        return list(res)

