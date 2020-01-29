class Solution:
    def isHappy(self, n: int) -> bool:
        def square(num):
            return sum([pow(int(x),2) for x in str(num)])
        slow,fast = n,n
        while True:
            slow = square(slow)
            fast = square(square(fast))
            if fast != slow:
                continue
            else:
                break
        return (fast == 1)