# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isBST(root,min_v,max_v):
            if not root:
                return 1
            if root.val <= min_v or root.val >= max_v:
                return 0
            res = isBST(root.left,min_v,root.val)
            res = res and isBST(root.right,root.val,max_v)
            return res
        return isBST(root,-sys.maxsize - 1,sys.maxsize)
