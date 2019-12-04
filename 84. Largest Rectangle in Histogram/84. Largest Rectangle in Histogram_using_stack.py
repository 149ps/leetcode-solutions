class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int: 
        stack = []
        area = 0
        stack.append(-1)
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                area = max(area,heights[stack.pop()] * (i - stack[-1] -1))
            stack.append(i)
        while stack[-1] != -1:
            area = max(area,heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return area