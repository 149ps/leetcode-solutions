# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        i = 0
        j = len(stack) - 1
        while i < j:
            if stack[i] != stack[j]:
                return False
            i += 1
            j -= 1
        return True