class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if w not in node.children:
                return False
            node = node.children[w]
        return True