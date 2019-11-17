class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2):
            p1 = i+1
            p2 = len(nums)-1
            while p1 < p2:
                sum = nums[i] + nums[p1] + nums[p2]
                if sum == 0 and not (nums[i], nums[p1],nums[p2]) in res:
                    res.add((nums[i], nums[p1],nums[p2]))
                    p1+=1
                    p2-=1
                elif sum < 0:
                    p1 += 1
                else:
                    p2 -= 1
        return res