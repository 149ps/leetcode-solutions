"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result, total, hmap = 0,0,{}
        for i in range(len(nums)):
            if nums[i] == 0:
                total -= 1
            else:
                total += 1
            if total == 0:
                result = i + 1
            if total not in hmap:
                hmap[total] = i
            else:
                if i - hmap[total] > result:
                    result = i - hmap[total]
        return result