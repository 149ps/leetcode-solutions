class Solution(object):
    def frequencySort(self, s):
        hash={}
        mystring=""
        for char in s:
            hash[char]=hash.get(char,0)+1
        x_sorted=sorted(hash.items(), key=operator.itemgetter(1),reverse=True)
        sorted_dict = collections.OrderedDict(x_sorted)
        for k,v in sorted_dict.items():
            for i in range(v):
                mystring+=str(k)
        return mystring
