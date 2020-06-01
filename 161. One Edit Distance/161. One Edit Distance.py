"""
Given two strings s and t, determine if they are both one edit distance apart.

Note:

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        def oneedit(s, t, flag):
            if not s and not t:
                if flag == 1:
                    return True
                else:
                    return False
            if not s and len(t) == 1 or not t and len(s) == 1:  # for case like 'ab' and 'ba'
                if flag == 0:
                    return True
                else:
                    return False
            if not s and len(t) > 1 or not t and len(s) > 1:
                return False
            if s[0] == t[0]:
                return oneedit(s[1:], t[1:], flag)
            elif s[0] != t[0]:
                if flag > 1:
                    return False
                else:
                    print("Flag", flag)
                    return oneedit(s[1:], t, flag + 1) or oneedit(s[1:], t[1:], flag + 1) or oneedit(s, t[1:], flag + 1)

        return oneedit(s, t, 0)