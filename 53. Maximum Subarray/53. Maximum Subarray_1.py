class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] > 0 :
                nums[i] += nums[i-1]
            maxSum = max(maxSum,nums[i])
        return maxSum