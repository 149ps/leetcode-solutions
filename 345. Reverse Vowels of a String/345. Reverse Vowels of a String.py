"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        i,j = 0,len(s) - 1
        list_s = list(s)
        while i < j:
            if list_s[i] in vowels and list_s[j] in vowels:
                list_s[i],list_s[j] = list_s[j],list_s[i]
                i += 1
                j -= 1
            elif list_s[i] in vowels and not list_s[j] in vowels:
                j -= 1
            else:
                i += 1
        return ''.join(list_s)