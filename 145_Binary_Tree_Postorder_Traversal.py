# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        def postorder(root,result):
            if not root:
                return
            postorder(root.left,result)
            postorder(root.right,result)
            result.append(root.val)
        postorder(root,result)
        return result
