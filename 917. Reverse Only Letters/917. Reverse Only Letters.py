class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i = 0
        j = len(S) - 1
        list_S = list(S)
        while i < j:
            if list_S[i] not in string.ascii_letters:
                i += 1
            elif list_S[j] not in string.ascii_letters:
                j -= 1
            else:
                temp = list_S[i]
                list_S[i] = list_S[j]
                list_S[j] = temp
                i += 1
                j -= 1
        return ''.join(list_S)