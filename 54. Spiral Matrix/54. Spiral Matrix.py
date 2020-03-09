"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        R,C = len(matrix)-1 , len(matrix[0])-1
        start_row,start_col = 0,0
        result = []
        while start_row <= R and start_col <= C:
            for i in range(start_col,C+1):
                result.append(matrix[start_row][i])
            start_row += 1
            for i in range(start_row,R+1):
                result.append(matrix[i][C])
            C -= 1
            if start_row <= R:
                for i in range(C,start_col-1,-1):
                    result.append(matrix[R][i])
                R -= 1
            if start_col <= C:
                for i in range(R,start_row-1,-1):
                    result.append(matrix[i][start_col])
                start_col += 1
        return result