# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        q = collections.deque()
        node = None
        q.append(root)
        value = root.val
        while q:
            node = q.popleft()
            if node.val == value:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                return False
        return True
        
