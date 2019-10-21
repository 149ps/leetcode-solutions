# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return None
        q = collections.deque()
        q.append(root)
        node = None
        min_val = 99999999999
        min_node = root.val
        while q:
            node = q.popleft()
            if (abs(node.val - target)) < min_val:
                min_val = abs(node.val - target)
                min_node = node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return min_node
