"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board,i,j):
            if i < 0 or j < 0 or i > len(board)-1 or j > len(board[0])-1 or board[i][j] != 'O':
                return
            board[i][j] = '$'
            dfs(board,i-1,j)
            dfs(board,i+1,j)
            dfs(board,i,j-1)
            dfs(board,i,j+1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board)-1:
                    dfs(board,i,j)
                if j == 0 or j == len(board[0]) - 1:
                    dfs(board,i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '$':
                    board[i][j] = 'O'