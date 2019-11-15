class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        lo = 0
        hi = len(A)-1
        while lo < hi:
            mid = lo + (hi-lo)//2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            if A[mid] < A[mid+1]:
                lo = mid+1
            if A[mid] > A[mid+1]:
                hi = mid - 1
        return lo