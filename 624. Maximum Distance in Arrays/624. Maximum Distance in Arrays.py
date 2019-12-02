class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res,min_number,max_number = 0,arrays[0][0],arrays[0][-1]
        for array in arrays[1:]:
            res = max(res,max(abs(max_number - array[0]),abs(array[-1] - min_number)))
            min_number = min(min_number,array[0])
            max_number = max(max_number,array[-1])
        return res