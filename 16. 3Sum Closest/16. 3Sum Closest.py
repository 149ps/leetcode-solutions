class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestsum = sys.maxsize
        for i in range(len(nums)-2):
            p1 = i+1
            p2 = len(nums)-1
            while p1 < p2:
                sum = nums[i] + nums[p1] + nums[p2]
                if abs(sum-target) < abs(closestsum-target):
                    closestsum = sum
                if sum < target:
                    p1+=1
                else:
                    p2-=1
        return closestsum