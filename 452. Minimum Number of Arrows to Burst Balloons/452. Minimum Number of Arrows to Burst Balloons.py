class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key= lambda a: a[1])
        print(points)
        end_coord = points[0][1]
        arrows = 1
        for point in points[1:]:
            if point[0] <= end_coord:
                continue
            else:
                arrows += 1
                end_coord = point[1]
        return arrows