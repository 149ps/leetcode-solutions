"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result,count = 1,1
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i] + 1:
                count += 1
                result = max(count,result)
            elif nums[i+1] == nums[i]:
                continue
            else:
                count = 1
        return result