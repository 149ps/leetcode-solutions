class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hmap = collections.Counter(nums)
        res = []
        for i in range(1,len(nums)+1):
            if not hmap.get(i):
                res.append(i)
        return res