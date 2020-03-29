"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hmap = {c:i for i,c in enumerate(order)}
        print(hmap)
        for word1,word2 in zip(words,words[1:]):
            if len(word1) > len(word2) and word1[:len(word2)] == word2: """ The second condition is for the case :: ["kuvp","q"]
"ngxlkthsjuoqcpavbfdermiywz". """
                return False
            for char1,char2 in zip(word1,word2):
                if hmap[char1] > hmap[char2]:
                    return False
                elif hmap[char1] == hmap[char2]:
                    continue
                else:
                    break
        return True