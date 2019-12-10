class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals
        intervals.sort(key= lambda a:a[0])
        stack = collections.deque()
        stack.append(intervals[0])
        for interval in intervals[1:]:
            if interval[0] <= stack[-1][1]:
                top = stack.pop()
                stack.append([top[0],max(top[1],interval[1])])
            else:
                stack.append(interval)
        return stack