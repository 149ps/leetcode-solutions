class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        maxreach,steps = nums[0],nums[0]
        jump = 1
        for i in range(1,len(nums)-1):
            maxreach = max(maxreach,nums[i]+i)
            steps -= 1
            if steps == 0:
                jump += 1
                steps = maxreach - i
        return jump