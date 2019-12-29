"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""
class NumArray:
    
    def __init__(self, nums: List[int]):
        self.lists = [0] * (len(nums)+1)
        total = 0
        for i,num in enumerate(nums):
            total += num
            self.lists[i+1] = total

    def sumRange(self, i: int, j: int) -> int:
        return self.lists[j+1] - self.lists[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)