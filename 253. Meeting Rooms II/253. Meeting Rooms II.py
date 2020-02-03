"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda a:a[0])
        active_rooms = []
        heapq.heapify(active_rooms)
        heapq.heappush(active_rooms,intervals[0][1])
        for interval in intervals[1:]:
            if interval[0] >= active_rooms[0]:
                heapq.heappop(active_rooms)
                heapq.heappush(active_rooms,interval[1])
            else:
                heapq.heappush(active_rooms,interval[1])
        return len(active_rooms)