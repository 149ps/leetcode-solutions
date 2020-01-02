class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        nums = [i  for i in range(1,10)]
        def backtrack(nums,index,n,k,path):
            if n < 0:
                return
            if k == 0 and n == 0:
                result.append(path)
                return
            for i in range(index,len(nums)):
                if nums[i] > n:
                    continue
                backtrack(nums,i+1,n-nums[i],k-1,path+[nums[i]])
        backtrack(nums,0,n,k,[])
        return result