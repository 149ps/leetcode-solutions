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

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count+=1
        def list_BST(start,end):
            nonlocal head
            if start > end:
                return None
            mid = (start + end)//2
            left = list_BST(start,mid-1)
            root = TreeNode(head.val)
            head = head.next
            root.left = left
            root.right = list_BST(mid+1,end)
            return root
        return list_BST(0,count-1)