class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        q = collections.deque(A)
        final = []
        while q:
            left = q[0]**2
            right = q[-1]**2
            if left < right:
                final.append(right)
                q.pop()
            else:
                final.append(left)
                q.popleft()
        return reversed(final)