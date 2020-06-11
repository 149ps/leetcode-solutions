class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def distance(x,y):
            return sqrt(x**2 + y**2)
        result = []
        min_heap = []
        heapq.heapify(min_heap)
        for x,y in points:
            heapq.heappush(min_heap,(distance(x,y),(x,y)))
        if len(min_heap) >= K:
            while K:
                result.append(heapq.heappop(min_heap)[1])
                K -= 1
        else:
            while min_heap:
                result.append(heapq.heappop(min_heap)[1])
        return result