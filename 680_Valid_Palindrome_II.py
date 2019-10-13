class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(0,len(s)-1):
            temp = s[:i] + s[i+1:]
            if temp == temp[::-1]:
                return True
        if s[:-1] == s[:-1][::-1]:
            return True
        return False
