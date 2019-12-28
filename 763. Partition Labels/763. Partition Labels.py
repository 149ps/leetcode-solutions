class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        hmap = {}
        for i,char in enumerate(S):
            hmap[char] = i
        start,end,res = 0,0,[]
        for i,char in enumerate(S):
            end = max(end,hmap[char])
            if i==end:
                res.append(i-start+1)
                start = i + 1
        return res