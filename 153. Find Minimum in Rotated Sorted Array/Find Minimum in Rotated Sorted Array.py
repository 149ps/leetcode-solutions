class Solution:
    def findMin(self, nums: List[int]) -> int:
        low,high = 0,len(nums)-1
        def min_element(arr,low,high):
            if high < low:
                return arr[0]
            if high==low:
                return arr[low]
            mid = (low+high)//2
            if mid < high and arr[mid+1] < arr[mid]:
                return arr[mid+1]
            if mid>low and arr[mid] < arr[mid-1]:
                return arr[mid]
            if arr[high] > arr[mid]:
                return min_element(arr,low,mid-1)
            return min_element(arr,mid+1,high)
        return min_element(nums,low,high)