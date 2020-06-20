class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def validate(s):
            stack = []
            for i in range(len(s)):
                if s[i] == '(':
                    stack.append(s[i])
                elif stack and s[i] == ')':
                    stack.pop()
                else:
                    return False
            return not stack

        result = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if validate(s[i:j + 1]):
                    result = max(result, j + 1 - i)
        return result