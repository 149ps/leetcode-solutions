class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list_t = list(t)
        for char in s:
            if char in s:
                list_t.remove(char)
        return list_t[-1]