class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        def dfs(string, temp_digits):
            if len(temp_digits) == 0:
                combinations.append(string)
                return
            for letter in phone[temp_digits[0]]:
                dfs(string+letter, temp_digits[1:])
        if not digits:
            return []
        combinations = []
        dfs('',digits)
        return combinations