# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        temp_str = ''
        temp = head
        while temp:
            temp_str += str(temp.val)
            temp = temp.next
        number = int(temp_str)
        temp_str = list(str(number+1))
        temp =  head
        while True:
            temp.val = temp_str[0]
            #print(temp.val,temp_str)
            del temp_str[0]
            #print(temp.next)
            if temp.next:
                temp = temp.next
            else:
                if temp_str:
                    x = ListNode(temp_str[0])
                    x.next = None
                    temp.next = x
                    break
                else:
                    break
        return head
            