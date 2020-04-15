class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hmap = collections.Counter(text)
        hmap_b = collections.Counter('balloon')
        count = 0
        while True:
            for k,v in hmap_b.items():
                if hmap[k] >= v:
                    hmap[k] -= v
                else:
                    return count
            count += 1
        return count
        