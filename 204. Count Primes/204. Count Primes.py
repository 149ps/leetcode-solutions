"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        nums = [1 for i in range(n)]
        nums[0], nums[1] = 0, 0
        p = 2
        while (p * p <= n):
            if nums[p] == 1:
                for i in range(p * 2, n, p):
                    nums[i] = 0
            p += 1
        return sum(nums)
