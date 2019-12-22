class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        leftmax = curmax = A[0]
        index = 0
        for i in range(1,len(A)):
            curmax = max(curmax,A[i])
            if A[i] < leftmax:
                leftmax = curmax
                index = i
        return index + 1