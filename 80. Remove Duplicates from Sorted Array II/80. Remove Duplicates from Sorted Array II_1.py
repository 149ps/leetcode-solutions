class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 0,1
        flag = 0
        while j < len(nums):
            if nums[j] == nums[j-1]:
                if flag != 1:
                    flag += 1
                    i += 1
                    nums[i] = nums[j]
            else:
                flag = 0
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1