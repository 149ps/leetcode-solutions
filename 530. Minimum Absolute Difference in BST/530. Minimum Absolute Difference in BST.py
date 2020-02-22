"""
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        q = collections.deque()
        node = None
        q.append(root)
        final_list = []
        while q:
            node = q.popleft()
            final_list.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        final_list.sort()
        min_diff = sys.maxsize
        for i in range(len(final_list)-1):
            min_diff = min(min_diff,abs(final_list[i] - final_list[i+1]))
        return min_diff