class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes = set()
        stack = []
        for i,c in enumerate(s):
            if c not in "()":
                continue
            if c == ")":
                if stack:
                    stack.pop()
                else:
                    indexes.add(i)
            if c == "(":
                stack.append(i)
        indexes = indexes.union(set(stack))
        final_str = ''
        for i,c in enumerate(s):
            if not i in indexes:
                final_str += c
        return final_str