"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
class Solution:

    def __init__(self, w: List[int]):
        self.array = w
        self.total_weight = sum(w)
        self.weighted_arr = []
        total = 0
        for weight in w:
            total += weight
            self.weighted_arr.append(total)
        #print(self.weighted_arr)

    def pickIndex(self) -> int:
        index = random.randrange(self.total_weight)
        return bisect.bisect(self.weighted_arr,index)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()