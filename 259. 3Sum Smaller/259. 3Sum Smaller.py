class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            p1 = i+1
            p2 = len(nums) - 1 
            while p1 < p2:
                sum = nums[i] + nums[p1] + nums[p2]
                if sum < target:
                    count += p2-p1
                    p1 += 1
                else:
                    p2 -= 1
        return count