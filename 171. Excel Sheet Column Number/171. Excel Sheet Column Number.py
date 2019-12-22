class Solution:
    def titleToNumber(self, s: str) -> int:
        tmp = list(reversed(list(s)))
        result = 0
        for i,char in enumerate(tmp):
            result += (26**i) * ((ord(char) - ord('A')) +1)
        return result