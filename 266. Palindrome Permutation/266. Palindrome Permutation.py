"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hmap = collections.Counter(s)
        count = 0
        for k,v in hmap.items():
            if v %2 != 0:
                count += 1
        return True if count <= 1 else False