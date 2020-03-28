"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        The idea here is if two sums have the same module and they are atleast two indexes apart then we can return true otherwise false.
         For [0,2],  k=2 prefix sum would be [0,2] and sum2 = 2 and sum1 = 0. sum2 - sum1 can be divided by k and the distance between those two indexes is atleast 2.
        """
        hmap = {0:-1} # initially at index -1 the sum would be zero.
        for i in range(1,len(nums)):
            nums[i] += nums[i-1] # prefix sum
        for i in range(len(nums)):
            temp = nums[i]
            if k:
                temp %= k 
            if temp in hmap.keys():
                if i - hmap[temp] >= 2:
                    return True
            else:
                hmap[temp] = i
        return False