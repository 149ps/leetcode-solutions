"""
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.



Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:



Remove the nodes with values 1, 2, and 3.

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]

Explanation:



Remove the nodes with value 1.

Example 3:

Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]

Explanation:



No node has value 5.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums, head):
        hset = set(nums)
        temp = ListNode(-100)
        temp.next = head
        result = temp
        while temp.next:
            if temp.next.val in hset:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return result.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Sample input for nums
nums = [1, 2, 3]

# Create an instance of the Solution class
solution = Solution()

# Call the modifiedList method, passing both nums and head
result = solution.modifiedList(nums, head)

# Print the modified linked list
while result:
    print(result.val)
    result = result.next