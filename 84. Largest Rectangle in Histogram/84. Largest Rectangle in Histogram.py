class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int: 
        def max_area(heights,start,end):
            if start > end:
                return 0
            min_index = start
            for i in range(start,end+1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(heights[min_index]*(end-start+1),max_area(heights,start,min_index-1),max_area(heights,min_index+1,end))
        return max_area(heights,0,len(heights)-1) 