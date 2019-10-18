class Solution:
    def isHappy(self, n: int) -> bool:
        def squarenum(num):
            sq_num = 0
            while num:
                sq_num += pow(num%10,2)
                num = num//10
            return sq_num
        slow,fast = n,n
        while True:
            slow = squarenum(slow)
            fast = squarenum(squarenum(fast))
            if slow != fast:
                continue
            else:
                break
        return (slow==1)
