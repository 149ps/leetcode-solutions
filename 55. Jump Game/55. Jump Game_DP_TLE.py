"""
Top Down DP TLE
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [-1 for i in range(len(nums))]
        memo[-1] = 1

        def canjump(i, nums):
            if memo[i] != -1:
                return True if memo[i] == 1 else False
            max_jump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, max_jump + 1):
                if canjump(j, nums):
                    memo[j] = 1
                    return True
            memo[i] = 0
            return False

        return canjump(0, nums)


