"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        if numRows==1:
            return [[1]]
        final = [[1]]
        for i in range(1,numRows):
            row = [1]
            for j in range(1,i):
                row.append(final[i-1][j-1] + final[i-1][j])
            row.append(1)
            final.append(row)
        return final