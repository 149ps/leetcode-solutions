class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        result,heap = [],[]
        heapq.heapify(heap)
        for i in range(len(nums1)):
            heapq.heappush(heap,(nums1[i]+nums2[0],i,0))
        while k > 0 and heap:
            total,i,j = heapq.heappop(heap)
            result.append([nums1[i],nums2[j]])
            if j + 1 < len(nums2): # why len(nums2) because heap size will already be equal to the size of len(nums1) (because of the first above for loop) so it can not be less than len(nums1) 
                heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
            k -= 1
        return result
