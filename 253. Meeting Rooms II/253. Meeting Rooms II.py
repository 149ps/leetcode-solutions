class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda a: a[0])
        active_rooms = []
        heapq.heapify(active_rooms)
        heapq.heappush(active_rooms,intervals[0][1])
        for interval in intervals[1:]:
            if active_rooms[0] <= interval[0]:
                heapq.heappop(active_rooms)
            heapq.heappush(active_rooms,interval[1])
        return len(active_rooms)