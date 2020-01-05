class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            result += [a + pow(2,i) for a in reversed(result)]
        return result