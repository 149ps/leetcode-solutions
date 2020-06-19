# BFS Solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(grid,i,j):
            q = collections.deque()
            q.append((i,j))
            while q:
                i,j = q.popleft()
                if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] != '1':
                    continue
                grid[i][j] = '#'
                q.append((i+1,j))
                q.append((i-1,j))
                q.append((i,j-1))
                q.append((i,j+1))
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    bfs(grid,i,j)
                    count += 1
        return count