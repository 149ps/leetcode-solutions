class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        percent_25 = len(arr)//4
        if len(arr) == 1:
            return arr[0]
        for i in range(len(arr)):
            if len(arr)%2 == 0:
                if arr[i] == arr[i+percent_25]:
                    return arr[i]
            else:
                if arr[i] == arr[i+percent_25+1]:
                    return arr[i]