class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        slow,fast = 0,len(s1)
        hmap = collections.Counter(s1)
        hmap_temp = collections.Counter(s2[slow:fast])
        while fast <= len(s2):
            if hmap == hmap_temp:
                return True
            hmap_temp[s2[slow]] -= 1
            if hmap_temp[s2[slow]] == 0:
                del hmap_temp[s2[slow]]
            if fast < len(s2):
                if hmap_temp.get(s2[fast]):
                    hmap_temp[s2[fast]] += 1
                else:
                    hmap_temp[s2[fast]] = 1
            slow += 1
            fast += 1
        return False