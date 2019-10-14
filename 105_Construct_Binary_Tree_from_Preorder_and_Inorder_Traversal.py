# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(preorder[0])
        rootpos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:rootpos+1],inorder[:rootpos])
        root.right = self.buildTree(preorder[rootpos+1:],inorder[rootpos+1:])
        return root
