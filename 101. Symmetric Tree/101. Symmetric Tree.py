"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def symmetric(root1, root2):
            if not root1 and not root2:
                return True
            if (not root1 and root2) or (root1 and not root2):
                return False
            if root1.val != root2.val:
                return False
            return symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left)

        return symmetric(root.left, root.right)