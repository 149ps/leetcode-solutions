class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        hmap = collections.Counter(A[0])
        temp_list = []
        for string in A[1:]:
            temp_hmap = collections.Counter(string)
            for k,v in hmap.items():
                if temp_hmap.get(k):
                    hmap[k] = min(hmap[k],temp_hmap[k])
                else:
                    temp_list.append(k)
        for k in temp_list:
            del hmap[k]
        return hmap.elements()