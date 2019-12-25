# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        q = collections.deque()
        node = None
        q.append(root)
        q.append(None)
        res = []
        temp = []
        while q:
            node = q.popleft()
            if node:
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                res.append(temp)
                temp = []
                if q:       # if there are still elements in a queue
                    q.append(None)
        return res