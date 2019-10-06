# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        p = collections.deque()
        q = collections.deque()
        q.append(root)
        q.append(None)
        node = None
        res = []
        temp = []
        while q:
            node = q.popleft()
            if node == None:
                p.append(temp)
                temp = []
                if q:
                    q.append(None)
            else:
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
        while p:
            res.append(p.pop())
        return res
        
