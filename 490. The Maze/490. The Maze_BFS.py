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
                row = i
                col = j
                while 0 <= row+x < len(maze) and 0 <= col+y < len(maze[0]) and maze[row+x][col+y]!=1:
                    row += x
                    col += y
                if maze[row][col] == 0:
                    Q.append([row,col])
        return False