class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for item in nums:
            if hmap.get(item):
                hmap[item] += 1
            else:
                hmap[item] = 1
        result = []
        heapq.heapify(result)
        for key,val in hmap.items():
            if len(result) < k:
                heapq.heappush(result,(val,key))
            else:
                if val > result[0][0]:
                    heapq.heapreplace(result,(val,key))
        return [arr[1] for arr in result]