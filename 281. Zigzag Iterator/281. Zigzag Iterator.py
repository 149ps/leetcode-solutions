"""
Given two 1d vectors, implement an iterator to return their elements alternately.

 

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6] 
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
 

Follow up:

What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].
"""
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.final = []
        self._v1 = v1[::-1]
        self._v2 = v2[::-1]
        flag = 0
        while self._v1 and self._v2:
            if not flag:
                self.final.append(self._v1.pop())
                flag = 1
            else:
                self.final.append(self._v2.pop())
                flag = 0
        if not self._v1:
            self.final.extend(self._v2[::-1])
        if not self._v2:
            self.final.extend(self._v1[::-1])
        self.index = 0

    def next(self) -> int:
        temp = self.index
        self.index += 1
        return self.final[temp]

    def hasNext(self) -> bool:
        return self.index < len(self.final)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())