# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        total = 0
        q = collections.deque()
        q.append((root, 0))
        while q:
            node, cur = q.popleft()
            cur = cur * 10 + node.val
            if not node.left and not node.right:
                total += cur
            if node.left:
                q.append((node.left, cur))
            if node.right:
                q.append((node.right, cur))
        return total

