class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        while lo < hi:
            mid = lo + (hi-lo)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                lo = mid+1
            elif nums[mid] < nums[mid-1]:
                hi = mid-1
        return lo