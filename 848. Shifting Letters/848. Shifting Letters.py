class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        result = ''
        shift = sum(shifts) % 26
        for i, char in enumerate(S):
            index = ord(char) - ord('a')
            result += chr(ord('a')+(index+shift)%26)
            shift = (shift - shifts[i]) % 26
        return result