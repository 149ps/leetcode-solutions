class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        min_element = min(A)
        sum = 0
        for char in str(min_element):
            sum += int(char)
        return 1 if sum%2==0 else 0
