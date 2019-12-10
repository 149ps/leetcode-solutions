class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        for interval in intervals:
            #if interval: [1,3]  and toberemoved: [0,2]
            if interval[0] < toBeRemoved[0] < interval[1]:
                result.append([interval[0],toBeRemoved[0]])
            # if interval[0,5] and toberemoved: [2,3]
            if interval[0] < toBeRemoved[1] < interval[1]:
                result.append([toBeRemoved[1],interval[1]])
            # if interval:[1,4] and toberemoved: [5,11] or interval: [7,10] and toberemoved: [1,6]
            if toBeRemoved[0] >= interval[1] or toBeRemoved[1] <= interval[0]:
                result.append(interval)
        return result