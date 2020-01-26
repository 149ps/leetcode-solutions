class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap, start, result = {},0,0
        for i,char in enumerate(s):
            if hmap.get(char) or hmap.get(char) == 0:
                result = max(result,i-start)
                start = max(start,hmap[char]+1) # why max? for string abba ans would be 3 instead of 2.
            hmap[char] = i
        return max(result,len(s)-start) # len(s) - start   if all the characters are distinct.