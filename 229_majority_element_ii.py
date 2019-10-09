class Solution(object):
    def majorityElement(self, nums):
        mylist=set()
        counter=collections.Counter()
        counter.update(nums)
        for i in counter:
            if counter[i] > len(nums)/3:
                mylist.add(i)
        return mylist
        
