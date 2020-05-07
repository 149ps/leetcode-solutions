"""
Given an array of integers nums, sort the array in ascending order.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quickSort(arr, low, high):
            if low < high:
                index = partition(arr, low, high)
                quickSort(arr, low, index - 1)
                quickSort(arr, index + 1, high)

        def partition(arr, l, h):
            i = l - 1
            pivot = arr[h]
            for j in range(l, h):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[h], arr[i + 1] = arr[i + 1], arr[h]
            return i + 1

        quickSort(nums, 0, len(nums) - 1)
        return nums

