"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1,10)]
        result = []
        def backtrack(nums,index,k,n,path):
            if n == 0 and k == 0:
                result.append(path)
                return
            if n < 0:
                return
            for i in range(index,len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if nums[i] > n:
                    continue
                backtrack(nums,i+1,k-1,n-nums[i],path+[nums[i]])
        backtrack(nums,0,k,n,[])
        return result