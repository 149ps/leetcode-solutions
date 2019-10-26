class Solution:
    def reverseWords(self, s: str) -> str:
        final_s = ''
        for word in s.split():
            final_s = final_s  + (word[::-1]) + ' '
        return final_s.rstrip()
