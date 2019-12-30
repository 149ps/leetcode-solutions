"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
"""
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        result,hmap,total = 0,{0:-1},0
        for i,num in enumerate(nums):
            total += num
            if total not in hmap.keys():
                hmap[total] = i
            if total-k in hmap.keys():
                result = max(result,i-hmap[total-k])
        return result