"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return [1]
        i = 0
        final = [[1]]
        while i != rowIndex+1:
            row = [1]
            for j in range(1,i):
                row.append(final[0][j-1] + final[0][j])
            row.append(1)
            final[:] = []
            final.append(row)
            i += 1
        return final[0]
