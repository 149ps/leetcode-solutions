class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(x,y):
            return (x**2+y**2)**(1/2)
        hmap = {}
        for x,y in points:
            hmap[x,y] = dist(x,y)
        hmap_sorted = sorted(hmap.items(),key = lambda a:a[1])
        return [key for key,value in hmap_sorted[:K]]