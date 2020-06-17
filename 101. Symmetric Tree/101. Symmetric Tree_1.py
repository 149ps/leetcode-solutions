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
        q = collections.deque()
        q.append(root)
        q.append(root)
        while q:
            node1 = q.popleft()
            node2 = q.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)
        return True