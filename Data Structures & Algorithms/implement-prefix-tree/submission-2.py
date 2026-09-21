class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isWord = False


    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if (c not in node.children):
                node.children[c] = PrefixTree()
            node = node.children[c]
        node.isWord = True
    def search(self, word: str) -> bool:
        node = self
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False

        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else: 
                return False
        return True
        