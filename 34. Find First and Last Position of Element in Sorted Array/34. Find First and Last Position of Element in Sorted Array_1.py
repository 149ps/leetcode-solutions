"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        left,right = 0,len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if 0 <= left <= len(nums)-1 and nums[left] == target:
            result.append(left)
        else:
            result.append(-1)
        left,right = 0,len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if 0 <= right <= len(nums)-1 and nums[right] == target:
            result.append(right)
        else:
            result.append(-1)
        return result