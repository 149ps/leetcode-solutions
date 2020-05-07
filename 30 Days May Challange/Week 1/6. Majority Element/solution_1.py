class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        for i,num in enumerate(nums):
            if nums[i + len(nums)//2] == num:
                return num