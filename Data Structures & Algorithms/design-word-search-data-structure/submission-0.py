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

        def dfs(index, node):

            if index == len(word):
                return node.isWord
            
            cha = word[index]

            if cha != '.':
                if cha not in node.children:
                    return False
                return dfs(index + 1, node.children[cha])

            else:
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
        
        return dfs(0, self.root)
