"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur = head
        hmap = {}
        while cur:
            if cur.val not in hmap:
                hmap[cur.val] = 1
            else:
                hmap[cur.val] += 1
            cur = cur.next
        cur = ListNode(-100)
        prev = cur
        for k,v in sorted(hmap.items()):
            if not v > 1:
                temp = ListNode(k)
                cur.next = temp
                cur = cur.next
        return prev.next