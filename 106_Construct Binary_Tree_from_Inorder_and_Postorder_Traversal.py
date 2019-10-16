# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        rootpos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:rootpos],postorder[:rootpos])
        root.right = self.buildTree(inorder[rootpos+1:],postorder[rootpos:-1])
        return root
