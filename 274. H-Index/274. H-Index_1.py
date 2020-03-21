class Solution:
    def hIndex(self, citations: List[int]) -> int:
        array = [0] * (len(citations)+1)
        result = 0
        for i in range(len(citations)):
            array[min(len(citations),citations[i])] += 1
        print(array)
        i = len(citations)
        s = array[len(citations)]
        while i > s:
            i -= 1
            s += array[i]
        return i