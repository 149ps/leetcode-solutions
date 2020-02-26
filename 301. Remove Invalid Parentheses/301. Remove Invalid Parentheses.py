"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""
class Solution:
    def removeInvalidParentheses(self, s):
        res = []
        self.visited = set([s])
        self.dfs(s, self.invalid(s), res)
        return res
    
    def dfs(self, s, n, res):
        if n == 0:
            res.append(s)
            return
        for i in range(len(s)):
            if s[i] in ('(',')'):
                new_s = s[:i]+s[i+1:]
                if new_s not in self.visited and self.invalid(new_s) < n:
                    self.visited.add(new_s)
                    self.dfs(new_s, self.invalid(new_s), res)
        
    def invalid(self, s):
        plus = minus = 0
        memo = {"(":1, ")":-1}
        for c in s:
            plus += memo.get(c,0)
            minus += 1 if plus < 0 else 0
            plus = max(0, plus)
        return plus + minus
        