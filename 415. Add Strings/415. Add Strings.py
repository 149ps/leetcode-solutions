"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result,carry = [],0
        i,j = len(num1)-1, len(num2)-1
        while i >= 0 or j >= 0:
            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            temp = n1 + n2 + carry
            result.append(str(temp%10))
            carry = temp // 10
            i -= 1 
            j -= 1
        if carry:
            result.append(str(carry))
        return ''.join(reversed(result))