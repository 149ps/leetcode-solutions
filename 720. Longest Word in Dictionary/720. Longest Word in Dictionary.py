class Solution:
    def longestWord(self, words: List[str]) -> str:
        longest_word = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(longest_word):
                if all(word[:i] in wordset for i in range(1,len(word))):
                    longest_word = word
            if len(word) == len(longest_word) and word < longest_word:
                if all(word[:i] in wordset for i in range(1,len(word))):
                    longest_word = word
        return longest_word