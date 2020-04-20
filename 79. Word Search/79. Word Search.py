"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
 

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(word,i,j):
            if not word:
                return True
            else:
                if i < 0 or j < 0 or i > len(board)-1 or j > len(board[0])-1 or board[i][j] != word[0]:
                    return
                temp = board[i][j]
                board[i][j] = '#'
                result = len(word) == 0 or dfs(word[1:],i+1,j) or dfs(word[1:],i-1,j) or dfs(word[1:],i,j-1) or dfs(word[1:],i,j+1)
                board[i][j] = temp
                return result
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(word,i,j):
                    return True
        return False