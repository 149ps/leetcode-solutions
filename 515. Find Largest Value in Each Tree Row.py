# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        q = collections.deque()
        q.append(root)
        q.append(None)
        node = None
        res = []
        temp = []
        while q:
            node = q.popleft()
            #print("node",node)
            if node == None:
                res.append(max(temp))
                #print("res",res)
                temp = []
                if q:
                    q.append(None)
            else:
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                #print("temp",temp)
        return res
