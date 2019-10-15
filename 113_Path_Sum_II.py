# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def pathsum(root,val,path):
            if not root:
                return []
            if (not root.left) and (not root.right):
                if root.val == val:
                    path.append(root.val)
                    paths.append(path)
            pathsum(root.left,val-root.val,path+[root.val])
            pathsum(root.right,val-root.val,path+[root.val])
            return paths
        global paths
        paths = []
        return pathsum(root,sum,[])
