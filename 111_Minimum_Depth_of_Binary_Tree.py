# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def depth_min(root):
            if not root:
                return 0
            if not root.left:
                return depth_min(root.right)+1
            if not root.right:
                return depth_min(root.left)+1
            return min(depth_min(root.left),depth_min(root.right)) + 1
        return depth_min(root)
