"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        R,C = n-1,n-1
        start_row,start_col = 0,0
        x = 1
        result = [[0]* (C + 1) for _ in range(R+1)]
        print(result)
        while start_col <= C and start_row <= R:
            for i in range(start_col,C+1):
                result[start_row][i] = x
                x += 1
            start_row += 1
            for i in range(start_row,R+1):
                result[i][C] = x
                x += 1
            C -= 1
            if start_row <= R:
                for i in range(C,start_col-1,-1):
                    result[R][i] = x
                    x += 1
                R -= 1
            if start_col <= C:
                for i in range(R,start_row-1,-1):
                    result[i][start_col] = x
                    x += 1
                start_col += 1
        return result