# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        currentlevel = []
        res = []
        lefttoright= True
        if root:
            currentlevel.append(root)
        while len(currentlevel)>0:
            levelres = []
            nextlevel = []
            while len(currentlevel)>0:
                node = currentlevel.pop()
                levelres.append(node.val)
                if lefttoright:
                    if node.left:
                        nextlevel.append(node.left)
                    if node.right:
                        nextlevel.append(node.right)
                else:
                    if node.right:
                        nextlevel.append(node.right)
                    if node.left:
                        nextlevel.append(node.left)
            currentlevel = nextlevel
            lefttoright = not lefttoright
            res.append(levelres)
        return res
