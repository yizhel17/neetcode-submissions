class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for cha in word:
            if cha not in cur.children:
                cur.children[cha] = TrieNode()
            cur = cur.children[cha]
        cur.isWord = True

        return None


    def search(self, word: str) -> bool:
        cur = self.root
        for cha in word:
            if cha not in cur.children:
                return False
            cur = cur.children[cha]
        
        return cur.isWord


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for cha in prefix:
            if cha not in cur.children:
                return False
            cur = cur.children[cha]
        
        return True
        