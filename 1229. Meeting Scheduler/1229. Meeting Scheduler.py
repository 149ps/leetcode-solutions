class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        i,j = 0,0
        while i < len(slots1) and j < len(slots2):
            start = max(slots1[i][0],slots2[j][0])
            end = min(slots1[i][1],slots2[j][1])
            if start <= end and (end - start)>= duration:
                return [start,start+duration]
            if slots1[i][1] <= slots2[j][1]:
                i += 1
            else:
                j += 1
        return []