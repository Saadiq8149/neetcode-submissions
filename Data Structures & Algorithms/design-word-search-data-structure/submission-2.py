class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True


    def search(self, word: str, root=None) -> bool:
        curr = self.root if root is None else root

        for i, c in enumerate(word):
            c = word[i]
            if c == ".":
                for children in curr.children.values():
                    if self.search(word[i+1:], children):
                        return True
                return False
            elif c not in curr.children:
                    return False
            curr = curr.children[c]

        return curr.endOfWord
            


