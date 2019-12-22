class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        temp_list = list(reversed(list(s)))
        for i in range(len(temp_list)):
            result += (ord(temp_list[i]) - ord('A') + 1) * (26**i)
        return result