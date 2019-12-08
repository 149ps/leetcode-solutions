class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key= lambda a: a[1])
        count, end = 0, intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < end:
                count += 1
            else:
                end = interval[1]
        return count