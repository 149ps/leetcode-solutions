# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        node = None
        q = collections.deque()
        q.appendleft(root)
        sum = 0
        while q:
            node = q.pop()
            if node.left:
                if node.left.left or node.left.right:
                    q.appendleft(node.left)
                else:
                    sum += node.left.val
            if node.right:
                q.appendleft(node.right)
        return sum
