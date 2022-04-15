"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return None
        q = collections.deque()
        q.append(root)
        result = None
        while q:
            n = len(q)
            for x in range(n):
                node = q.popleft()
                if x == 0:
                    result = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result