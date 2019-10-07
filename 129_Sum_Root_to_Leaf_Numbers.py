# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        Cur = 0
        Sum = [0]
        def cal_sum(root,Cur,Sum):
            if not root:
                return
            Cur = Cur*10 + root.val
            if not root.left and not root.right:
                Sum[0]+=Cur
                return
            cal_sum(root.left,Cur,Sum)
            cal_sum(root.right,Cur,Sum)
        cal_sum(root,Cur,Sum)
        return Sum[0]
