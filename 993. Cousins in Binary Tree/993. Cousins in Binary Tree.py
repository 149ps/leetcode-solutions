"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = collections.deque()
        d = 0
        x_level = y_level = 0
        x_parent = y_parent = -100
        q.append([root,d,-1])
        while q:
            length = len(q)
            d += 1
            for i in range(length):
                node,level,parent = q.popleft()
                if node.val == x:
                    x_level = level
                    x_parent = parent
                elif node.val == y:
                    y_level = level
                    y_parent = parent
                if node.left:
                    q.append([node.left,d,node.val])
                if node.right:
                    q.append([node.right,d,node.val])
            if x_level and y_level:
                if x_level == y_level and x_parent != y_parent:
                    return True
                else:
                    return False