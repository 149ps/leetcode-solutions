# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth_max(root):
            if not root:
                return 0
            return max(depth_max(root.left),depth_max(root.right)) + 1
        return depth_max(root)
