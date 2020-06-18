"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s_list = list(s.lower())
        # print(s_list)
        i, j = 0, len(s_list) - 1
        while i < j:
            while i < j and not s_list[i].isalnum():
                i += 1
            while i < j and not s_list[j].isalnum():
                j -= 1
            if s_list[i] != s_list[j]:
                return False
            i += 1
            j -= 1
        return True