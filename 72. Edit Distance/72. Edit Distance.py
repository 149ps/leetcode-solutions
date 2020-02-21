"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def md( word1, word2,cache ={}):
            if not word1 and not word2:
                return 0
            if not len(word1)   or not len(word2):
                return len(word1) or len(word2)
            if word1[0]==word2[0]:
                return md(word1[1:],word2[1:])
            if (word1,word2) not in cache:
                inserted = 1+ md(word1[1:],word2)
                deleted  = 1+ md(word1,word2[1:])
                replaced = 1+ md(word1[1:],word2[1:])
                cache[(word1,word2)]= min(inserted,deleted,replaced)
            return cache[(word1,word2)]
        return md(word1,word2,{})