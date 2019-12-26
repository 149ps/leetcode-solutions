"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Ex:3

IP: [[1,4],[2,3]]
OP: [[1,4]]
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda a:a[0])
        stack = collections.deque()
        stack.append(intervals[0])
        for interval in intervals[1:]:
            if interval[0] <= stack[-1][1]:
                temp = stack.pop()
                stack.append([temp[0],max(interval[1],temp[1])]) # why do we need max here? See, example 3.
            else:
                stack.append(interval)
        return stack