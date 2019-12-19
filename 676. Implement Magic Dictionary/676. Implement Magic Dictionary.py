"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = None
        
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        
        for word in dict:
            node = self.root
            for letter in word:
                if letter not in node.children:
                    node.children[letter] = TrieNode()
                node = node.children[letter]
            node.end = True
                

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return self.dfs(word,self.root,0)
    
    def dfs(self,word,root,flag):
        node = root
        if len(word) == 0:
            if flag == 1:
                return node.end == True
            else:
                return False
        result = False
        for key in node.children:
            if key == word[0]:
                result = result or self.dfs(word[1:],node.children[key],flag)
            else:
                if flag == 0:
                    result = result or self.dfs(word[1:],node.children[key],1)
                else:
                    continue
        return result
#Good Problem. Revise this again and again.                
        
            
            
            


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)