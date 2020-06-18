class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        heapq.heapify(max_heap)
        for num in nums:
            heapq.heappush(max_heap,(-1)*num)
        while k > 1:
            heapq.heappop(max_heap)
            k -= 1
        return (-1)*max_heap[0]