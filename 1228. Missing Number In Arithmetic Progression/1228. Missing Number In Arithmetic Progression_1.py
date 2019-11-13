class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = (max(arr) - min(arr))//len(arr)
        for i in range(len(arr)-1):
            if not abs(arr[i] - arr[i+1]) == diff:
                return arr[i]-diff if arr[i]>arr[i+1] else arr[i]+diff
        return 0