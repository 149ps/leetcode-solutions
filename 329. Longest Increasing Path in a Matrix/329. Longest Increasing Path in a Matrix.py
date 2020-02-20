"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(i,j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(dfs(i+1,j) if i < len(matrix) - 1 and val < matrix[i+1][j] else 0,
                                   dfs(i-1,j) if i > 0 and val < matrix[i-1][j] else 0,
                                   dfs(i,j+1) if j < len(matrix[0])-1 and val < matrix[i][j+1] else 0,
                                   dfs(i,j-1) if j > 0 and val < matrix[i][j-1] else 0)
            return dp[i][j]
        if not matrix:
            return 0
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        return max(dfs(x,y) for x in range(len(matrix)) for y in range(len(matrix[0])))
