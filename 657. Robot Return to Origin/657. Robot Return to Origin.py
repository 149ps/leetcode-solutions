class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = [0,0]
        for c in moves:
            if c == 'U':
                start[1] += 1
            elif c == 'D':
                start[1] -= 1
            elif c == 'L':
                start[0] -= 1
            elif c == 'R':
                start[0] += 1
        if start[0] != 0 or start[1] != 0:
            return False
        else:
            return True