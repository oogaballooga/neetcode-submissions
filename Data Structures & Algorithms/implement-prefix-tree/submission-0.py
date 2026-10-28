class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.isWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for l in word:
            if l not in cur.children:
                return False
            cur = cur.children[l]
        return cur.isWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for l in prefix:
            if l not in cur.children:
                return False
            cur = cur.children[l]
        return True