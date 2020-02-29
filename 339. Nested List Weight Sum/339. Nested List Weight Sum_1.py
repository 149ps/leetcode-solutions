#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        depth,total = 1,0 
        q = collections.deque()
        for i in nestedList:
            q.append((i,depth))
        while q:
            next_item,depth = q.popleft()
            if next_item.isInteger():
                total += (next_item.getInteger() * depth)
            else:
                for i in next_item.getList():
                    q.append((i,depth+1))
        return total