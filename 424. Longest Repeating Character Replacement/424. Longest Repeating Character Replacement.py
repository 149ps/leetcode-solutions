"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start,end = 0,0
        result,hmap = 0,{}
        cur_count,max_count = 0,0 # max_count to keep track of element whose count is highest till we have watched elements. cur_count is the count of current element.
        for end in range(len(s)):
            if hmap.get(s[end]):
                hmap[s[end]] += 1
            else:
                hmap[s[end]] = 1
            cur_count = hmap[s[end]]
            max_count = max(max_count,cur_count) # if cur_count is greater than the max_count, update it.
            while (end - start + 1 > k + max_count): # if our sliding window is greater than k+ max_count, increase the start pointer until it becomes smaller.
                hmap[s[start]] -= 1
                start += 1
            result = max(result,end-start+1) # keep updating the result with start and end pointer
        return result