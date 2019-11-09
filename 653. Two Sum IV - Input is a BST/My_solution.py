# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        q = collections.deque()
        q.appendleft(root)
        node = None
        all_val = []
        while q:
            node = q.pop()
            all_val.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        hmap={}
        for i,v in enumerate(all_val):
            temp = k-v
            if temp in hmap.keys():
                return True
            hmap[v] = i
        return False