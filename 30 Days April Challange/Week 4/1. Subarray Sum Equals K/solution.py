"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result,total,hmap = 0,0,{}
        for num in nums:
            hmap[total] = hmap.get(total,0) + 1
            total += num
            if hmap.get(total-k):
                result += hmap[total-k]
        return result