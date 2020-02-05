class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        Q = collections.deque()
        Q.append(start)
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while Q:
            i,j = Q.popleft()
            maze[i][j] = '#'
            if [i,j] == destination:
                return True
            for x,y in dirs:
                row = i + x
                col = j + y
                while 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col]!=1:
                    row += x
                    col += y
                row -= x
                col -= y
                if maze[row][col] == 0:
                    Q.append([row,col])
        return False