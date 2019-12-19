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
    
    def search(self):
        result = ''
        node = self.root
        while node:
            # return when reaches the end of word or when there are more than 1 branches
            if node.end or len(node.children) > 1:
                return result
            c = list(node.children)[0]
            result += c
            node = node.children[c]
                    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        trie = Trie()
        for string in strs:
            trie.addWord(string)
        return trie.search()