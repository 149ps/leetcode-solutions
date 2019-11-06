class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr,start,end):
            while(start<end):
                temp = arr[start]
                arr[start] = arr[end]
                arr[end] = temp
                start+=1
                end-=1
            return arr
        reverse(nums,0,len(nums)-(k%len(nums))-1)
        reverse(nums,len(nums)-(k%len(nums)),len(nums)-1)
        reverse(nums,0,len(nums)-1)
        return nums