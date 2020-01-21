class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap,hmap_index = {},{}
        for i,char in enumerate(s):
            if hmap.get(char):
                hmap[char] += 1
                hmap_index[char] = i
            else:
                hmap[char] = 1
                hmap_index[char] = i
        for i,char in enumerate(s):
            if hmap[char] == 1:
                return hmap_index[char]
        return -1

"""
One Hashtable for storing count and other hashtable for storing indexes.
"""