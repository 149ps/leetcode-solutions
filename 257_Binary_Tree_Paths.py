# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def path_appender(root,path,paths):
            if not root:
                return 0
            path+=str(root.val)
            if (not root.left) and (not root.right):
                paths.append(path)
            path_appender(root.left,path+'->',paths)
            path_appender(root.right,path+'->',paths)
            return paths
        paths=[]
        path_appender(root,'',paths)
        return paths
