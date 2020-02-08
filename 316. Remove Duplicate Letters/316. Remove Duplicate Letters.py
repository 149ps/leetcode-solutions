"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_index = {char:i for i,char in enumerate(s)}
        for i,char in enumerate(s):
            if char not in seen:
                """
                Need to first see if the char is already seen or not. If seen no need to bother otherwise we'll check.
                """
                while stack and char < stack[-1] and i < last_index[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(char)
                stack.append(char)
        return ''.join(stack)
