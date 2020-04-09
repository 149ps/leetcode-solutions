"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hmap = {}
        for word in wordList:
            for i in range(len(word)):
                if hmap.get(word[:i] + '_' + word[i+1:]):
                    hmap[word[:i] + '_' + word[i+1:]].append(word)
                else:
                    hmap[word[:i] + '_' + word[i+1:]] = [word]
        q = collections.deque([(beginWord,1)])
        visited = set()
        while q:
            word,k = q.popleft()
            if word == endWord:
                return k
            if word not in visited:
                visited.add(word)
                for i in range(len(word)):
                    temp = word[:i] + '_' + word[i+1:]
                    if hmap.get(temp):
                        for neighbor in hmap[temp]:
                            if neighbor not in visited:
                                q.append((neighbor,k+1))
        return 0