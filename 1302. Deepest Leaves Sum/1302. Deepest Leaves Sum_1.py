"""
Alternate solution using BFS. No need to find max_depth first and then do BFS. You can do that on the go.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append((root,0))
        max_depth = 0
        result = 0
        while q:
            node,depth = q.popleft()
            if not node.left and not node.right:
                if depth > max_depth:
                    result = node.val
                    max_depth = depth
                elif depth == max_depth:
                    result += node.val
            if node.left:
                q.append((node.left,depth+1))
            if node.right:
                q.append((node.right,depth+1))
        return result