class Solution(object):
    def reverseVowels(self, s):
        i,j = 0,len(s) - 1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        list_s = list(s)
        while i < j :
            if list_s[i] in vowels and list_s[j] in vowels:
                temp = list_s[i]
                list_s[i] = list_s[j]
                list_s[j] = temp
                i += 1
                j -= 1
            elif not list_s[i] in vowels:
                i += 1
            elif not list_s[j] in vowels:
                j -= 1
        return ''.join(list_s)