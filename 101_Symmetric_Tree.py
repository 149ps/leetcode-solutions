# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        def symmetric(root1,root2):
            if (root1 is None) and (root2 is None):
                return True
            elif (root1 and root2):
                return (root1.val == root2.val) and symmetric(root1.left,root2.right) and symmetric(root1.right,root2.left)
            else:
                return False
        return symmetric(root.left,root.right)
