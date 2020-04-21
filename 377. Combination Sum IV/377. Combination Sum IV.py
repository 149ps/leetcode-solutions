"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        def backtrack(nums,index,total):
            nonlocal count
            if total < 0:
                return
            if total == 0:
                count += 1
                print(count)
                return
            for i in range(len(nums)):
                if nums[i] > total:
                    return
                backtrack(nums,i,total-nums[i])
        backtrack(nums,0,target)
        return count