class Solution:
    def isHappy(self, n: int) -> bool:
        hmap = {}
        while n!=1:
            n = sum([pow(int(x),2) for x in str(n)])
            if n in hmap.keys():
                if hmap[n]:
                    return False
            else:
                hmap[n] = 1
        return True
