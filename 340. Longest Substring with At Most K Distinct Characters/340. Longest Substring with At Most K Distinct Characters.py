class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        hmap,result = {},0
        i,j = 0,0
        while j < len(s):
            if not s[j] in hmap:
                if not len(hmap) < k:
                    min_char = min(hmap, key=hmap.get)
                    i = hmap[min_char] + 1
                    del hmap[min_char]
            hmap[s[j]] = j
            result = max(j - i + 1,result)
            j += 1
        return result