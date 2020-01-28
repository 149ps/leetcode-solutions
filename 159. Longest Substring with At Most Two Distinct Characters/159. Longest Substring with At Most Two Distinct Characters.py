"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hmap = {}
        i,j,result = 0,0,0
        while j < len(s):
            if len(hmap) <= 2:
                hmap[s[j]] = j
            if len(hmap) == 3:
                index = min(hmap.values())
                hmap.pop(s[index])
                i = index + 1
            j += 1
            result = max(result,j-i)
        return result