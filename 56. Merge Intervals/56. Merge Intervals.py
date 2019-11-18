class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        def takefirst(li):
            return li[0]
        intervals.sort(key=takefirst)
        stack = collections.deque()
        stack.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] > stack[-1][1]:
                stack.append(intervals[i])
            elif intervals[i][0] <= stack[-1][1]:
                top = stack[-1]
                top[1] = max(intervals[i][1],stack[-1][1])
                stack.pop()
                stack.append(top)
        return stack