class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 1
        num_set = set(nums)
        for num in num_set:
            cur_num,count = num,1
            while cur_num + 1 in num_set:
                count += 1
                cur_num += 1
            result = max(result,count)
        return result