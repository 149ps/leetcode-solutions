"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        def bin_search(arr,low,high,target):
            if low>high:
                return -1
            mid = (high-low) + low//2 # to avoid interger overflow
            if arr[mid] == target:
                return mid
            elif arr[low] <= arr[mid]:
                if target >= arr[low] and target <= arr[mid]:
                    return bin_search(arr,low,mid-1,target)
                return bin_search(arr,mid+1,high,target)
            else:
                if target >= arr[mid] and target <=arr[high]:
                    return bin_search(arr,mid+1,high,target)
                return bin_search(arr,low,mid-1,target)
        return bin_search(nums,start,end,target) 