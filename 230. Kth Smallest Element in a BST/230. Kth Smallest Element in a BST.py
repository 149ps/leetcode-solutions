# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        q = collections.deque()
        q.appendleft(root)
        arr = []
        node = None
        while q:
            node = q.pop()
            if node:
                arr.append(node.val)
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
        return sorted(arr)[k-1]
