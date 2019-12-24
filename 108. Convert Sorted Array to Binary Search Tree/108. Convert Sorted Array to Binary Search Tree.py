"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def BST(arr,left,right):
            if left> right:
                return None
            elif left == right:
                node = TreeNode(arr[left])
                node.right = None
                node.left = None
            else:
                mid = left + (right - left)//2
                node = TreeNode(arr[mid])
                node.left = BST(arr,left,mid-1)
                node.right = BST(arr,mid+1,right)
            return node
        return BST(nums,0,len(nums)-1)