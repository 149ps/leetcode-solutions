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
        memo = [[0 for _ in range(len(grid[0])+1)] for _ in range(len(grid)+1)]
        def minpath(grid,i,j,memo):
            if i == len(grid) or j == len(grid[0]):
                memo[i][j] = sys.maxsize
                return memo[i][j]
            if not memo[i][j]:
                if i == len(grid)-1 and j == len(grid[0])-1:
                    memo[i][j] = grid[i][j]
                    return memo[i][j]
                memo[i][j] = grid[i][j] + min(minpath(grid,i+1,j,memo),minpath(grid,i,j+1,memo))
            return memo[i][j]
        return minpath(grid,0,0,memo)
        
