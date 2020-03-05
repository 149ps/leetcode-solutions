"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import collections
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        heapq.heapify(min_heap)
        head = cur = ListNode(0)
        for l in lists:
            if l:
                heapq.heappush(min_heap,(l.val,id(l),l))
        while min_heap:
            val,nodeid,node = heapq.heappop(min_heap)
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(min_heap,(node.val,id(node),node))
        return head.next