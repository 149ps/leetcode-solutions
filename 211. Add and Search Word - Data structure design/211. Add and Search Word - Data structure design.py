class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.end = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        for i,letter in enumerate(word):
            if letter == '.':
                for child in node.children:
                    temp_trie = WordDictionary()
                    temp_trie.root = node.children[child]
                    if temp_trie.search(word[i+1:]):
                        return True
            elif letter not in node.children:
                return False
            node = node.children[letter]
        return node.end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)