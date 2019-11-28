class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda a:a[1])
        print("Trips:",trips)
        temp_capacity = trips[0][0]
        end_location = []
        heapq.heapify(end_location)
        heapq.heappush(end_location,(trips[0][2],trips[0][0]))
        for i in range(1,len(trips)):
            if end_location[0][0] > trips[i][1]: 
                if (temp_capacity + trips[i][0]) > capacity:
                    return False
                else:
                    temp_capacity += trips[i][0]
                    heapq.heappush(end_location,(trips[i][2],trips[i][0]))
                #print(end_location)
            else:
                while end_location[0][0] <= trips[i][1]:
                    x = heapq.heappop(end_location)
                    temp_capacity -= x[1]
                    if temp_capacity < 0:
                        temp_capacity = 0
                    if not end_location:
                        break
                temp_capacity += trips[i][0]
                heapq.heappush(end_location,(trips[i][2],trips[i][0]))
        print(end_location)
        return True
            
            
        