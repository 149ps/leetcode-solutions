class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]
        for i in range(n):
            temp = [x + pow(2,i) for x in reversed(result)]
            result += temp
            temp = []
        return result