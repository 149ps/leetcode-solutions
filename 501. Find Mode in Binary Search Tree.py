# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        q = collections.deque()
        hmap = {}
        modes = []
        q.appendleft(root)
        node = None
        while q:
            node = q.pop()
            if node:
                hmap[node.val] = hmap.get(node.val,0) + 1
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        #print(hmap)
        max_val = max(hmap.items(), key=lambda x: x[1])
        #print(max_val)
        for k,v in hmap.items():
            if v == max_val[1]:
                modes.append(k)
        return modes
