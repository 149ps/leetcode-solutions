class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hmap = collections.defaultdict(int)
        res = 0
        for t in time:
            if hmap.get((60-t%60)%60):
                res +=  hmap[(60-t%60)%60]
            hmap[t%60] +=1
        return res