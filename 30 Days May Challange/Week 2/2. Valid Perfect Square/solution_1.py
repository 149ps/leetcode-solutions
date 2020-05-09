class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left,right = 0,num - 1
        while left <= right:
            mid = left + (right - left)//2
            temp = mid ** 2
            if temp > num:
                right = mid - 1
            elif temp < num:
                left = mid + 1
            else:
                return True
        return left ** 2 == num