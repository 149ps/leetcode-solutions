"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        q = collections.deque()
        node = None
        if not root:
            return None
        q = collections.deque()
        node = None
        q.append(root)
        q.append(None)
        res = []
        temp = []
        while q:
            node = q.popleft()
            if node:
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            else:
                res.append(temp)
                temp = []
                if q:       # if there are still elements in a queue
                    q.append(None)
        return reversed(res)
        