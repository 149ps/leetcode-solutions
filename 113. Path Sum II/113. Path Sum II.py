"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []

        def pathsum(root, total, path):
            nonlocal result
            if not root:
                return None
            if not root.left and not root.right:
                if root.val == total:
                    result.append(path + [root.val])
                    return
            left = pathsum(root.left, total - root.val, path + [root.val])
            right = pathsum(root.right, total - root.val, path + [root.val])

        pathsum(root, sum, [])
        return result