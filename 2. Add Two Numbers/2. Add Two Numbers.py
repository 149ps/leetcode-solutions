"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1,head2 = l1,l2
        temp = ListNode(-100)
        cur = temp
        carry,total = 0,0
        while head1 or head2:
            a = head1.val if head1 else 0
            b = head2.val if head2 else 0
            cur_total = a + b + carry
            carry = cur_total // 10
            temp.next = ListNode(cur_total % 10)
            temp = temp.next
            if head1:
                head1 = head1.next
            if head2:
                head2  = head2.next
        if carry:
            temp.next = ListNode(carry)
        return cur.next