# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        gset = set(G)
        temp = head
        res = 0
        while temp:
            if (temp.val in gset and
                    getattr(temp.next, 'val', None) not in gset):
                res += 1
            temp = temp.next
        return res