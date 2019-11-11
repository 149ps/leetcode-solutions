class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        hmap={}
        for i,row in enumerate(mat):
            hmap[i] = collections.Counter(row)
        for k,v in hmap[0].items():
            if hmap[1].get(k) and hmap[2].get(k):
                return k
        return -1