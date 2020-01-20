"""
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""
# 31/40 test cases passed
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        first_missing,last_missing = "",""
        hash_set = set(nums)
        final_list = []
        for num in range(lower,upper+1):
            if num not in hash_set:
                if len(first_missing)>0:
                    last_missing = str(num)
                else:
                    first_missing = str(num)
            if num >= upper or num in hash_set:
                if len(first_missing) and len(last_missing):
                    final_list.append(str(first_missing) + "->" + str(last_missing))
                elif first_missing and not last_missing:
                    final_list.append(str(first_missing))
                first_missing,last_missing = "",""
        return final_list