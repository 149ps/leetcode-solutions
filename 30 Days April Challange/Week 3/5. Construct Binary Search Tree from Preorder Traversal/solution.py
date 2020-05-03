"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

 

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = []
        stack.append(root)
        """
        The first node will be the root node and after that for each and every node we check if it is greater than top of stack or not, if no, we will make a node of that value and make the left child of the element which is on top of stack. If yes we pop the elements until we find the element greater than the current value or while stack is not empty. If we find the element then this element's right child will be current valued node. 
        """
        for val in preorder[1:]:
            if val < stack[-1].val:
                stack[-1].left = TreeNode(val)
                stack.append(stack[-1].left) # can't do stack.append(TreeNode(val)) since we will not have links.Similar for right child as well.
            else:
                while stack and val >= stack[-1].val:
                    temp = stack.pop()
                temp.right = TreeNode(val)
                stack.append(temp.right)
        return root