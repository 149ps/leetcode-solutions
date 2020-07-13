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
        m = len(grid)
        n = len(grid[0])
        dirs = [(0,-1),(0,1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for dx,dy in dirs:
                        if 0 <= i + dx <= len(grid)-1 and 0 <= j + dy <= n-1:
                            if grid[i+dx][j+dy] == 0:
                                result += 1
                        if i + dx < 0 or i + dx > m-1 and 0 <= j + dy <= n-1:
                            result += 1
                        if j + dy < 0 or j + dy > n-1 and 0 <= i + dx <= m-1:
                            result += 1
        return result