"""
Solution using Maxheap
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        max_heap,result = [],''
        heapq.heapify(max_heap)
        hmap = collections.Counter(s)
        for key,val in hmap.items():
            heapq.heappush(max_heap,(-val,key))
        while max_heap:
            freq,char = heapq.heappop(max_heap)
            result += ((-1)*freq * char)
        return result