"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        hmap = {}
        i,j,result = 0,0,0
        while j < len(s):
            if len(hmap) <= k:
                hmap[s[j]] = j
            if len(hmap) == k+1:
                index = min(hmap.values())
                hmap.pop(s[index])
                i = index + 1
            j += 1
            result = max(result,j-i)
        return result