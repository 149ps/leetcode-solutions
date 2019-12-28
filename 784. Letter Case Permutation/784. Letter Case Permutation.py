"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = ['']
        for ch in S:
            temp = []
            for i in result:
                if ch.isdigit():
                    temp.append(i+ch)
                else:
                    temp.append(i+ch.upper())
                    temp.append(i+ch.lower())
                result = temp
        return result