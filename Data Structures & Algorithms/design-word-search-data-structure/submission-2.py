class TrieNode:

    def __init__(self):
        from collections import defaultdict
        self.children = defaultdict(TrieNode)
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for cha in word:
            cur = cur.children[cha]
        cur.isWord = True
        

    def search(self, word: str) -> bool:
        def dfs(ind, node):
            # Base case
            if ind == len(word):
                return node.isWord
            
            if word[ind] == ".":
                for let in node.children.values():
                    if dfs(ind + 1, let):
                        return True
                return False
            
            else:
                if word[ind] not in node.children:
                    return False
                return dfs(ind + 1, node.children[word[ind]])
        
        return dfs(0, self.root)