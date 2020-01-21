class Solution(object):
    def firstUniqChar(self, s):
        counter=collections.Counter(s)
        for char in s:
            if counter[char]==1:
                return s.index(char)
        return -1
