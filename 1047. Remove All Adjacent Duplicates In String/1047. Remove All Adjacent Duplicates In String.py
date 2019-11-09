class Solution:
    def removeDuplicates(self, S: str) -> str:
        q = collections.deque()
        for char in S:
            if q and char == q[-1]:
                q.pop()
            else:
                q.append(char)
        return ''.join(q)