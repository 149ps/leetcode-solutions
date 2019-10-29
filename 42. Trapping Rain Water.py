class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left_arr = []
        right_arr = []
        for i in range(len(height)):
            left_arr.append(max(height[:i+1]))
        for i in range(len(height),0,-1):
            right_arr.append(max(height[i-1:]))
        right_arr = right_arr[::-1]
        for i in range(len(height)):
            result += (min(left_arr[i],right_arr[i]) - height[i])
        return result
