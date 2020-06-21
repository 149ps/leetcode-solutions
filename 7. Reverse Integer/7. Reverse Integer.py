"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x: int) -> int:
        symbol = 1
        if x < 0:
            symbol = -1
            x = -x
        temp = 0
        while x:
            temp = temp * 10 + (x % 10)
            x = x // 10
        return temp * symbol if temp < pow(2, 31) else 0