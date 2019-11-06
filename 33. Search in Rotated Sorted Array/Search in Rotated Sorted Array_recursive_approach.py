class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        def bin_search(arr,low,high,target):
            if low>high:
                return -1
            mid = (low+high)//2
            if arr[mid] == target:
                return mid
            if arr[low] <= arr[mid]:
                if target >= arr[low] and target <= arr[mid]:
                    return bin_search(arr,low,mid-1,target)
                return bin_search(arr,mid+1,high,target)
            if arr[mid]<=arr[high]:
                if target >= arr[mid] and target <=arr[high]:
                    return bin_search(arr,mid+1,high,target)
                return bin_search(arr,low,mid-1,target)
        return bin_search(nums,start,end,target)