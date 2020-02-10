"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
				"""
				If Any element is zero then proceed with the next steps o/w ignore
				"""
                if matrix[i][j] == 0:
                    row = i
                    col = j
                    for x,y in neighbors: # In vertical and horizontal directions, we will go till the end of the row and column. While loop is there for doing the same thing. 
                        row += x
                        col += y
                        while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
                            if matrix[row][col] != 0: 
							"""	
							we need to take care about this check. If the number is not already zero then and then we'll change it to zero.If it is already zero then we don't want to change it since we will also have to remove it's corresponding numbers.
							"""
                            matrix[row][col] = sys.maxsize
                            row += x
                            col += y
                        row = i
                        col = j
		"""
		We'll check if any number is sys.maxsize, if it is then we'll simply replace it with zero
		"""
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == sys.maxsize:
                    matrix[i][j] = 0