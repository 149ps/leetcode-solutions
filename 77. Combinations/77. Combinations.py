"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums = [i for i in range(1,n+1)]
        print(nums)
        def backtrack(nums,index,k,path):
            if k < 0:
                return
            if k == 0:
                result.append(path)
                return
            for i in range(index,len(nums)):
                backtrack(nums,i+1,k-1,path+[nums[i]])
        backtrack(nums,0,k,[])
        return result