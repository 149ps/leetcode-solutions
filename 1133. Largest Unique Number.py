class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        return max([k for k,v in collections.Counter(A).items() if v==1]) if [k for k,v in collections.Counter(A).items() if v==1] else -1
