# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        q = collections.deque()
        total=0
        q.appendleft(root)
        node = None
        while q:
            node = q.pop()
            if node.val >= L and node.val <= R:
                total+=node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return total