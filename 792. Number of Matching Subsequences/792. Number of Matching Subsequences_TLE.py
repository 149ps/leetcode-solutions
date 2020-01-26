"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input: 
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        def issub(s,t):
            if not s and t:
                return True
            if s and not t:
                return False
            if not s and not t:
                return True
            count = 0
            for i,char in enumerate(t):
                if char == s[count]:
                    count+=1
                if count >= len(s):
                    return True
            return False
        final_count = 0
        for word in words:
            if issub(word,S):
                final_count+=1
        return final_count