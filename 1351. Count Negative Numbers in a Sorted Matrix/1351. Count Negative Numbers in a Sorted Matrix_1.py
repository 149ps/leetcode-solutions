class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def binsearch(row):
            start,end = 0,len(row) - 1
            while start <= end:
                mid = start + (end - start)//2
                if row[mid] < 0:
                    end = mid - 1
                else:
                    start = mid + 1
            return len(row) - start
        count = 0
        for row in grid:
            count += binsearch(row)
        return count