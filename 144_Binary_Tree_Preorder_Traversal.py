# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def inorder(root,result):
            if not root:
                return
            inorder(root.left,result)
            result.append(root.val)
            inorder(root.right,result)
        inorder(root,result)
        return result
