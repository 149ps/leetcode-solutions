class Solution:
    def dfs(self, left, right,s):
        final = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            final += 1
        return final

    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += self.dfs(i,i,s)
            result += self.dfs(i,i+1,s)
        return result