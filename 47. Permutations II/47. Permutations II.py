"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution:
    def permuteUnique(self, nums):
        result = []
        visited = [False] * len(nums)
        nums.sort()
        def backtrack(nums,path):
            if len(nums) == len(path):
                result.append(path)
                return
            for i in range(len(nums)):
                if not visited[i]:
                    if i > 0 and not visited[i-1] and nums[i-1] == nums[i]:
                        continue
                    visited[i] = True
                    backtrack(nums,path+[nums[i]])
                    visited[i] = False
        backtrack(nums,[])
        return result