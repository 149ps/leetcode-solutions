# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        q = collections.deque()
        node = None
        q.append(root)
        q.append(None)
        curSum = 0
        count = 0
        result = []
        while q:
            node = q.popleft()
            if node == None:
                result.append(float(curSum)/float(count))
                count=0
                curSum=0
                if q:
                    q.append(None)
            else:
                curSum += node.val
                count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result
