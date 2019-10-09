# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def preorder(root,result):
            if not root:
                return
            result.append(root.val)
            preorder(root.left,result)
            preorder(root.right,result)
        preorder(root,result)
        return result
