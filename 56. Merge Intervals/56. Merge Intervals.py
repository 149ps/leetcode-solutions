class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals
        intervals.sort(key= lambda x: x[0])
        stack = collections.deque()
        stack.append(intervals[0])
        for i in range(1,len(intervals)):
            if intervals[i][0] <= stack[-1][1]:
                top = stack[-1]
                stack.pop()
                stack.append([top[0],max(top[1],intervals[i][1])])
            else:
                stack.append(intervals[i])
        return stack