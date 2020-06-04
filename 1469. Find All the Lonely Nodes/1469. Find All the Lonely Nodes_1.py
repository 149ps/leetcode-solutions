# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        result = []

        def func(root):
            nonlocal result
            if not root:
                return None
            if not root.left and root.right:
                result.append(root.right.val)
            if root.left and not root.right:
                result.append(root.left.val)
            func(root.left)
            func(root.right)
        func(root)
        return result