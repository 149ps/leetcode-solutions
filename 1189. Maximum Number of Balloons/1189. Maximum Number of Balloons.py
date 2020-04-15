"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap = {}
        for char in text:
            hmap[char] = hmap.get(char,0) + 1
        return min(hmap.get('b',0),
                   hmap.get('a',0),
                   hmap.get('l',0)//2,
                   hmap.get('o',0)//2,
                   hmap.get('n',0))