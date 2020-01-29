"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a,b = headA,headB
        lenA,lenB = 0,0
        while a:
            lenA += 1
            a = a.next
        while b:
            lenB += 1
            b = b.next
        a,b = headA,headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                a = a.next
        elif lenB > lenA:
            for i in range(lenB-lenA):
                b = b.next
        while a != b:
            a = a.next
            b = b.next
        return b