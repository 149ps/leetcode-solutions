class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos_word1,pos_word2 = len(words)+1, len(words)+1
        min_D = 10000
        for index,word in enumerate(words):
            if word == word1:
                pos_word1 = index
            if word == word2:
                pos_word2 = index
            if (pos_word1 != len(words)+1) and (pos_word2 != len(words)+1):
                min_D = min(min_D,abs(pos_word1 - pos_word2))
        return min_D
