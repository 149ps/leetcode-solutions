# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def BST(A,left,right):
            if left>right:
                return None
            if left==right:
                temp_node = TreeNode(A[left])
                temp_node.left = None
                temp_node.right = None
            else:
                mid = left + (right-left)//2
                temp_node = TreeNode(A[mid])
                temp_node.left = BST(A,left,mid-1)
                temp_node.right = BST(A,mid+1,right)
            return temp_node
        return BST(nums,0,len(nums)-1)