class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap={}
        for index,val in enumerate(nums):
            temp = target - val
            if temp in hmap.keys():
                return (hmap[temp],index)
            hmap[val] = index 