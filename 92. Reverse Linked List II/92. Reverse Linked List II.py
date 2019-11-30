# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        cur,prev,count = head, None, 1
        while count < m:
            prev = cur
            cur = cur.next
            count += 1
        tail, con, nxt = cur, prev, None
        while count <= n:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count+=1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head
            
        