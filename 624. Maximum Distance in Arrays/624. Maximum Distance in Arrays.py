class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        diff = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        for array in arrays[1:]:
            diff = max(diff,max(abs(max_val-array[0]),abs(array[-1] - min_val)))
            min_val = min(min_val,array[0])
            max_val = max(max_val,array[-1])
        return diff