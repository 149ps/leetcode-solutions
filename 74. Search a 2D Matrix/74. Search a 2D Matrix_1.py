class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        lo = 0
        hi = row * col - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_element = matrix[mid//col][mid%col]
            if mid_element == target:
                return True
            elif  target > mid_element:
                lo = mid + 1
            elif target < mid_element:
                hi = mid - 1
        return False