# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p,q = l1,l2
        new_head = ListNode(0)
        curr = new_head
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0 
            total_sum = x+y+carry
            carry = total_sum // 10 
            curr.next = ListNode(total_sum % 10)
            curr = curr.next
            if p != None:
                p = p.next 
            if q != None:
                q  = q.next 
            if carry > 0:
                curr.next = ListNode(carry)
        return new_head.next
