"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hmap,left_index,right_index,degree,result = {},{},{},1,len(nums)
        for i,num in enumerate(nums):
            if num not in left_index.keys():
                left_index[num] = i
            right_index[num] = i
            if hmap.get(num):
                hmap[num] += 1
                degree = max(degree,hmap[num])
            else:
                hmap[num] = 1
        for num in nums:
            if hmap[num] == degree:
                result = min(result,right_index[num]-left_index[num]+1)
        return result