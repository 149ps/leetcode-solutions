"""
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        result = []
        def dfs(node):
            level = 0
            nonlocal result
            if not node:
                return 0
            level = max(dfs(node.left),dfs(node.right)) + 1
            if len(result) < level:
                result.append([])
            result[level-1].append(node.val)
            return level
        dfs(root)
        return result