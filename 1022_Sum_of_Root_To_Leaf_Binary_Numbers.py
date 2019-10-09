# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        Cur_str = ''
        Sum = [0]
        def cal_sum(root,current,Sum):
            if not root:
                return 0
            current += str(root.val)
            if (not root.left) and (not root.right):
                Sum[0]  += int(current,2)
            cal_sum(root.left,current,Sum)
            cal_sum(root.right,current,Sum)
        cal_sum(root,Cur_str,Sum)
        return Sum[0]
            
        
