class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Calculate the frequency of all the elements in an array.
        hmap = collections.Counter(nums)
        # Create a max_heap of size n. (We can create a max_heap using min_heap by multiplying frequency by -1.)
        max_heap = [(-v,k) for k,v in hmap.items()]
        heapq.heapify(max_heap)
        #pop k elements from max_heap.
        return [heapq.heappop(max_heap)[1] for _ in range(k)]