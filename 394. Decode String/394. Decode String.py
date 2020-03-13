"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
class Solution:
    def decodeString(self, s: str) -> str:
        result = []
        for i in s:
            if i == ']':
                temp,count = [],[]
                while result and result[-1] != '[':
                    temp.append(result.pop())
                if result:
                    result.pop()
                while result and '0' <= result[-1] <= '9':
                    count.append(result.pop())
                result.append(int(''.join(count[::-1])) * ''.join(temp[::-1]))
            else:
                result.append(i)
        return ''.join(result)
