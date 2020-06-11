"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

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
