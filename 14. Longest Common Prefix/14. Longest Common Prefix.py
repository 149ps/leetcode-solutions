class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self,word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.end = True
    
    def prefix(self):
        node = self.root
        lcp = ''
        while node:
            if node.end or len(node.children) > 1:
                return lcp
            char = list(node.children)[0]
            lcp += char
            node = node.children[char]
            
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        trie = Trie()
        for word in strs:
            trie.add(word)
        return trie.prefix()