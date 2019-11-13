class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        arr.sort()
        diff = (arr[-1] - arr[0])//len(arr)
        for i in range(1,len(arr)):
            if not arr[i] == arr[i-1]+diff:
                return arr[i-1] + diff
        return 0