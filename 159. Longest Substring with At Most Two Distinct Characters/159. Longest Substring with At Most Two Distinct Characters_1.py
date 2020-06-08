class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hmap = {}
        i,j = 0,0
        count,result = 0,0
        while i < len(s) and j < len(s):
            if not s[j] in hmap:
                if not len(hmap) < 2:
                    min_char = min(hmap, key=hmap.get)
                    i = hmap[min_char] + 1
                    del hmap[min_char]
            hmap[s[j]] = j
            result = max(j - i + 1,result)
            j += 1
        return result