"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]


Constraints:

10 <= low <= high <= 10^9
"""
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q = collections.deque(range(1,10))
        result = []
        while q:
            item = q.popleft()
            if low <= item <= high:
                result.append(item)
            elif high < item:
                return result
            last_digit = item % 10
            if last_digit < 9: q.append(item* 10 + (last_digit+1))
        return result