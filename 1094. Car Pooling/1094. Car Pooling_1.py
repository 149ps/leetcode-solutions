class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda a: a[1])
        end_location = []
        heapq.heapify(end_location)
        cur_capacity = 0
        max_capacity = 0
        for num , start, end in trips:
            while end_location and start >= end_location[0][0]:
                cur_capacity -= end_location[0][1]
                heapq.heappop(end_location)
            heapq.heappush(end_location,(end,num))
            cur_capacity += num
            max_capacity = max(max_capacity,cur_capacity)
        return max_capacity <= capacity