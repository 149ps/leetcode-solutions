class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        hmap = collections.Counter(nums)
        return [key for key in hmap.keys() if hmap[key]==1]