class TrieNode:
    def __init__(self):
        self.children = {} # letter : TrieNode()
        self.isWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()       

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode() 
            node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        # search for whole word first bfs
        node = self.root
        def dfs(j, cur):
            for i in range(j, len(word)):
                c= word[i]
                if c == ".":
                    # go through children and dfs with child
                    # from sub problem i+1 : n
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isWord
        return dfs(0, self.root)

        # def bfs(c, isLast, queue):
        #     found = False
        #     res = []
        #     while(queue):
        #         node = queue.pop(0)
        #         if len(node.children) == 0:
        #             print("NO KIDS")
        #             return [False,[]]
        #         print(c, node.children)
        #         # wildcard
        #         if c == ".":
        #             #move to next level
        #             # add all children to q
        #             for child in node.children.values():
        #                 res.append(child)
        #                 if isLast:
        #                     node = child
                            
        #                     print(node.isWord)
        #                     found |= node.isWord
        #                 else:
        #                     found = True
        #         # search through tree
        #         elif c in node.children:
        #             # found cur -> move to next node in Trie
        #             node = node.children[c]
        #             if isLast:
        #                 print(node.isWord)
        #                 found |= node.isWord
        #             else:
        #                 res.append(node)
        #                 found = True
        #         else:
        #             # cannot find character at this pos
        #             found |= False
        #     return [found, res]
        # q = [node]

        # for i, c in enumerate(word):
        #     last = (i == len(word) -1)
        #     found, q = bfs(c, last, q)
        #     if found == False:
        #         return False
        # print("finish")
        # return True

# queue ad, ad, ad
# b d m
# a a a
# d d d
        
                
        
        
# Prefix tree
# d a y
# b a y
# m a y
# if . -> can move on to the next level of anytree
# need to track levels
# search should be made in bfs then
# for .
# lets setup 
# search full word . is just any. letter


