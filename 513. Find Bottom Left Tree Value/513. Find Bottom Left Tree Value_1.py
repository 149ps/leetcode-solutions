# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        bottom_left, max_depth = root.val, 0

        def bottom(root, depth):
            nonlocal bottom_left
            nonlocal max_depth
            if not root:
                return None
            if depth > max_depth:
                max_depth = depth
                bottom_left = root.val
            bottom(root.left, depth + 1)
            bottom(root.right, depth + 1)

        bottom(root, 0)
        return bottom_left