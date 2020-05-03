"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        table = copy.copy(grid)
        table[0][0] = grid[0][0]
        for i in range(1,len(grid)):
            table[i][0] = table[i-1][0] + grid[i][0]
        for j in range(1,len(grid[0])):
            table[0][j] = table[0][j-1] + grid[0][j]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                table[i][j] = grid[i][j] + min(table[i][j-1],table[i-1][j])
        return table[-1][-1]