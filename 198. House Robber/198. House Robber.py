class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max,cur_max = 0,0
        for num in nums:
            temp = cur_max
            cur_max = max(prev_max+num,cur_max)
            prev_max = temp
        return cur_max