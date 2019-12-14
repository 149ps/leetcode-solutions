class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob(nums):
            cur_max,prev_max = 0,0
            for num in nums:
                temp = cur_max
                cur_max = max(cur_max,prev_max+num)
                prev_max = temp
            return cur_max
        return max(rob(nums[1:]),rob(nums[:-1]))