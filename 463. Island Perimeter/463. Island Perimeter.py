"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    if n == 0 or grid[m][n-1] == 0: result += 1
                    if n == len(grid[0]) - 1 or grid[m][n+1] == 0: result += 1
                    if m == 0 or grid[m-1][n] == 0: result += 1
                    if m == len(grid) - 1  or grid[m+1][n] == 0: result += 1
        return result