class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('','', string.punctuation)).replace(" ","").lower()
        reversed_s = s[::-1]
        if s == reversed_s:
            return True
        else:
            return False
