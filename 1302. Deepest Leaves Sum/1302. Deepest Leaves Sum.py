"""
Given a binary tree, return the sum of values of its deepest leaves.
 

Example 1:



Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        d = 0

        def depth(root):
            nonlocal d
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            d = max(d, max(left, right))
            return max(left, right) + 1

        depth(root)
        q = collections.deque()
        q.append((root, 0))
        result = 0
        while q:
            node, height = q.popleft()
            if node.left:
                q.append((node.left, height + 1))
            if node.right:
                q.append((node.right, height + 1))
            if not node.left and not node.right and height == d:
                result += node.val
        return result