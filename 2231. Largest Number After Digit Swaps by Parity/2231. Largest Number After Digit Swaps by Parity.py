"""
You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.



Example 1:

Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
Example 2:

Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.


Constraints:

1 <= num <= 109
"""
class Solution:
    def largestInteger(self, num: int) -> int:
        odd,even,odd_nums,even_nums = set(),set(),[],[]
        for i,digit in enumerate(str(num)):
            if int(digit) % 2 == 0:
                even.add(i)
                even_nums.append(int(digit))
            else:
                odd.add(i)
                odd_nums.append(int(digit))
        odd_nums.sort(reverse=True)
        even_nums.sort(reverse=True)
        result,o,e = [],0,0
        for i in range(len(str(num))):
            if i in odd:
                result.append(str(odd_nums[o]))
                o += 1
            elif i in even:
                result.append(str(even_nums[e]))
                e += 1
        return int(''.join(result))