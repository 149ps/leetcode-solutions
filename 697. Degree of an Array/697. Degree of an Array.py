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
        hmap,left,right = collections.Counter(nums),{},{}
        result = len(nums)
        degree = max(hmap.values())
        for i,num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
        for num in nums:
            if hmap[num] == degree:
                result = min(result,right[num]-left[num]+1)
        return result