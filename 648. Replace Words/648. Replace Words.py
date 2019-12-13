class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self,word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.end = True
        
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dict:
            trie.add(root)
        def replace(word):
            node = trie.root
            temp_s = ''
            for w in word:
                if w not in node.children:
                    break
                node = node.children[w]
                temp_s += w
                if node.end:
                    return temp_s
            return word
        return ' '.join(map(replace,sentence.split()))
        