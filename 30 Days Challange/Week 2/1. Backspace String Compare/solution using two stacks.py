"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = []
        t_stack = []
        for i,char in enumerate(S):
            if not char == '#':
                s_stack.append(char)
            else:
                if s_stack:
                    s_stack.pop()
                else:
                    continue
        for i,char in enumerate(T):
            if not char == '#':
                t_stack.append(char)
            else:
                if t_stack:
                    t_stack.pop()
                else:
                    continue
        if len(s_stack) == len(t_stack):
            if all([s_stack[i] == t_stack[i] for i in range(len(s_stack))]):
                return True
            else:
                return False
        else:
            return False