class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        i,j = 0,0
        while i < len(A) and j < len(B):
            start = max(A[i][0],B[j][0])
            end = min(A[i][1],B[j][1])
            if start <= end:
                result.append([start,end])
            if A[i][1] >= B[j][1]:
                j += 1
            else:
                i += 1
        return result