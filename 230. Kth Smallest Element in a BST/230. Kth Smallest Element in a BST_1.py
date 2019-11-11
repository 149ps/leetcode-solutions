# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = []
        def inorder(root,result):
            if not root:
                return 
            inorder(root.left,result)
            result.append(root.val)
            inorder(root.right,result)
            return result
        return inorder(root,result)[k-1]