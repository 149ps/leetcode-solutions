class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parantheses = { ')': '(', '}':'{',']':'['}
        for char in s:
            if char in parantheses.keys():
                head = stack.pop() if stack else '#'
                if parantheses[char] != head:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0