class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        hmap = dict(collections.Counter(nums1))
        for num in nums2:
            if hmap.get(num):
                result.append(num)
                hmap[num] -= 1
        return result