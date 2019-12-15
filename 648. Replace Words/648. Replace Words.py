class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self,word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.end = True
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dict:
            trie.addWord(root)
        def replaceRoot(word):
            node = trie.root
            temp_str = ''
            for letter in word:
                if letter not in node.children:
                    break
                node = node.children[letter]
                temp_str += letter
                if node.end:
                    return temp_str
            return word
        return ' '.join(map(replaceRoot,sentence.split(' ')))