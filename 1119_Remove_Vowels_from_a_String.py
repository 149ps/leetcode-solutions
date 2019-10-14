class Solution:
    def removeVowels(self, S: str) -> str:
        vowels = ['a','e','i','o','u']
        res = ''
        for char in S:
            if not char in vowels:
                res+=char
        return res
