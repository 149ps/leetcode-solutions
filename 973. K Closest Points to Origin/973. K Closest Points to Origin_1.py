class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(x,y):
            return (x**2+y**2)**(1/2)
        minheap = []
        heapq.heapify(minheap)
        for x,y in points:
            heapq.heappush(minheap,(dist(x,y),[x,y]))
        return [heapq.heappop(minheap)[1] for k in range(K)]