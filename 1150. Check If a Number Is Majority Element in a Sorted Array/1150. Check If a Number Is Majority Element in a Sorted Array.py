class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        for i in range(len(nums)//2):
            if nums[len(nums)//2 -1]==target:
                return True
        return False