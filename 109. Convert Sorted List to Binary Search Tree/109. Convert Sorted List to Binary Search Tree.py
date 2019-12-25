# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        temp,count = head,0
        while temp:
            temp = temp.next
            count += 1
        def BST(start,end):
            nonlocal head
            if start > end:
                return None
            mid = start + (end - start)//2
            left = BST(start,mid-1)
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = BST(mid+1,end)
            return root
        return BST(0,count-1)